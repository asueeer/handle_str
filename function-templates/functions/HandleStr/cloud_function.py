import json

import re
import json

from multiprocessing import Process, Pipe
from multiprocessing.connection import wait


class Pool:
    """Naive implementation of a process pool with mp.Pool API.

    This is useful since multiprocessing.Pool uses a Queue in /dev/shm, which
    is not mounted in an AWS Lambda environment.
    """

    def __init__(self, process_count=1):
        assert process_count >= 1
        self.process_count = process_count

    @staticmethod
    def wrap_pipe(pipe, index, func):
        def wrapper(args):
            try:
                result = func(args)
            except Exception as exc:  # pylint: disable=broad-except
                result = exc
            pipe.send((index, result))

        return wrapper

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass

    def map(self, function, arguments):
        pending = list(enumerate(arguments))
        running = []
        finished = [None] * len(pending)
        while pending or running:
            # Fill the running queue with new jobs
            while len(running) < self.process_count:
                if not pending:
                    break
                index, args = pending.pop(0)
                pipe_parent, pipe_child = Pipe(False)
                process = Process(
                    target=Pool.wrap_pipe(pipe_child, index, function),
                    args=(args,))
                process.start()
                running.append((index, process, pipe_parent))
            # Wait for jobs to finish
            for pipe in wait(list(map(lambda t: t[2], running))):
                index, result = pipe.recv()
                # Remove the finished job from the running list
                running = list(filter(lambda x: x[0] != index, running))
                # Add the result to the finished list
                finished[index] = result

        return finished


def get_batches(s, w):
    batches = []
    batch_text = ""
    w_count = 0
    for i in range(len(s)):
        batch_text += s[i]
        if i == 0 and s[i].isalpha():
            w_count += 1
            continue
        if i == len(s) - 1:
            batches.append(batch_text)
            continue
        if s[i].isalpha():
            if s[i - 1].isalpha() is False:
                w_count += 1
        else:
            if w_count == w:
                batches.append(batch_text)
                w_count = 0
                batch_text = ""
    return batches


def count_pattern(batches, p) -> (list, int):
    count = 0
    count_list = []
    for batch in batches:
        occurrences = len(re.findall(pattern=p, string=batch))
        count_list.append(occurrences)
        count += occurrences
    return count_list, count


def get_remove_list(count_list, m, r):
    remove_list = []
    diff = r - m
    for count in count_list:
        remove_times = min(diff, count)
        remove_list.append(remove_times)
        diff -= remove_times
    return remove_list


def trim(s):
    for i in range(len(s)):
        if s[i].isalpha():
            return s[i:]
    return ""


def do_remove(arg):
    text = arg['text']
    p = arg['p']
    remove_times = arg['remove_times']
    if remove_times == 0:
        return text
    new_str = re.sub(pattern=p, repl='', count=remove_times, string=text)
    return trim(new_str)


def remove_pattern(batches, p, remove_list) -> list:
    args = []
    for i in range(len(batches)):
        args.append({
            'text': batches[i],
            'p': p,
            'remove_times': remove_list[i]
        })
    pool = Pool(10)
    return pool.map(do_remove, args)


def handle_str(s, p, w, m) -> (int, str):
    batches = get_batches(s, w)
    count_list, r = count_pattern(batches, p)
    if r <= m:
        return r, s

    remove_list = get_remove_list(count_list, m, r)
    new_batches = remove_pattern(batches, p, remove_list)
    next_str = ''.join(new_batches)
    return r, next_str


def cloud_function(json_input):
    s = json_input.get('inputStr')
    p = json_input.get('pattern')
    w = int(json_input.get('wordNum'))
    m = int(json_input.get('threshold'))

    # Processing
    count, next_s = handle_str(s, p, w, m)
    # return the result
    res = {
        "Count": count,
        "NextStr": next_s
    }
    return res
