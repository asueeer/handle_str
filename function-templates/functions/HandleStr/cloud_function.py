import json

import re
import json


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


def get_remove_list(count_list, m):
    remove_list = []
    diff = m
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


def do_remove(text, p, remove_times):
    if remove_times == 0:
        return text
    new_str = re.sub(pattern=p, repl='', count=remove_times, string=text)
    return trim(new_str)


def remove_pattern(batches, p, remove_list) -> list:
    for i in range(len(batches)):
        batches[i] = do_remove(batches[i], p, remove_list[i])
    return batches


def handle_str(s, p, w, m) -> (int, str):
    batches = get_batches(s, w)
    count_list, r = count_pattern(batches, p)
    if r <= m:
        return r, s

    remove_list = get_remove_list(count_list, m)
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
