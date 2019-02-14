#!/bin/env python3

import datetime
import json

statistics = {}


def benchmethod(func):
    def method(*args, **kwargs):
        name = func.__name__
        start = datetime.datetime.now()
        result = func(*args, **kwargs)
        stop = datetime.datetime.now()
        duration = stop - start
        if name not in statistics:
            statistics[name] = {
                "docstring": func.__doc__,
                "durations": [duration.total_seconds()],
            }
        else:
            statistics[name]["durations"].append(duration.total_seconds())
        return result

    return method


def report():

    res = ""
    for key in statistics:
        data = statistics[key]
        durations = data["durations"]
        data["min"] = min(durations)
        data["max"] = max(durations)
        data["average"] = sum(durations) / len(durations)
        s = "{}\n{} {}\n".format(key, data["average"], data["docstring"])
        res += s
    res = json.dumps(statistics)
    print(res)
