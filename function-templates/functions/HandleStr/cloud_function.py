from do_handle import *


def cloud_function(json_input):
    s = json_input["inputStr"]
    p = json_input["pattern"]
    w = json_input["wordNum"]
    m = json_input["threshold"]

    # Processing
    count, next_s = handle_str(s, p, w, m)
    # return the result
    res = {
        "Count": count,
        "NextStr": next_s
    }
    return res
