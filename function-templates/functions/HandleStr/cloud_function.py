from do_handle import *
import json


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
