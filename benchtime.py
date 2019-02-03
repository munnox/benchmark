#!/bin/env python3

import datetime

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
                "durations": [
                    duration.total_seconds()
                ]
            }
        else:
            statistics[name]['durations'].append(
                duration.total_seconds()
            )
        return result
    return method

def report():
    
    res = ""
    for key in statistics:
        data = statistics[key]
        s = "{}\n{} {}\n".format(key, sum(data['durations'])/len(data['durations']), data['docstring'])
        res += s
    print(res)   
