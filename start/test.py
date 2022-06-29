from handle_str import *

if __name__ == '__main__':
    s = 'one one one two one'
    p = 'one'
    w = 2
    m = 2

    batches = get_batches(s, w)
    count_list, r = count_pattern(batches, p)
    print("r:", r)
    print("count_list:", count_list)
    if r <= m:
        exit(0)

    remove_list = get_remove_list(count_list, m, r)
    print("remove_list:", remove_list)
    new_batches = remove_pattern(batches, p, remove_list)
    next_str = ''.join(new_batches)
    print(new_batches)
    print("next_str:", next_str)

    print(handle_str(s, p, w, m))
