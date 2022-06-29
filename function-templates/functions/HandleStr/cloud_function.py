from do_handle import *
import json


def cloud_function(json_input):
    body = json.loads(json_input.get('body'))
    s = body.get('inputStr')
    p = body.get('pattern')
    w = int(body.get('wordNum'))
    m = int(body.get('threshold'))

    # Processing
    count, next_s = handle_str(s, p, w, m)
    # return the result
    res = {
        "Count": count,
        "NextStr": next_s
    }
    return res
