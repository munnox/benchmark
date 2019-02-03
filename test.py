#!/bin/env python3

import benchtime

KB = 2**10
MB = 2**10 * KB
GB = 2**10 * MB

@benchtime.benchmethod
def processorbound():
    "Processor Bound squaring x for 10000 tries"
    for x in range(1000):
        for n in range(500):
            x**n

@benchtime.benchmethod
def processormemorybound():
    "Processor memory bound concat 1KB strings into 1GB strings"
    x = "SPAM"*int((KB/4))
    print("Length: {} KB".format(len(x)/KB))
    # for _ in range(10):
    y = x*MB
    print("Length: {} GB".format(len(y)/GB))

@benchtime.benchmethod
def storagebound():
    "Processor memory bound concat 1KB strings into 1GB strings write then read from file"
    x = "SPAM"*int((KB/4))
    print("Length: {} KB".format(len(x)/KB))
    # for _ in range(10):
    y = x*MB
    print("Length: {} GB".format(len(y)/GB))
    with open("tmp", "w") as f:
        f.write(y)
    del y
    with open("tmp", "r") as f:
        y = f.read()
    print("Length: {} GB".format(len(y)/GB))
    

for _ in range(10):
    processorbound()

for _ in range(10):
    processormemorybound()

for _ in range(10):
    storagebound()

# print(benchtime.statistics)
benchtime.report()
# print(benchtime.info)
