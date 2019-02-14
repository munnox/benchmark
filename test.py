#!/bin/env python3

import sys
import benchtime
import unittest


KB = 2 ** 10
MB = 2 ** 10 * KB
GB = 2 ** 10 * MB

SPAM_1KB = "SPAM" * int((KB / 4))


class TestProcessorOperations(unittest.TestCase):
    @benchtime.benchmethod
    def processorbound(self):
        "Processor bound test do X^N where X=(0,10000) and N=(0,500)."
        for x in range(1000):
            for n in range(500):
                x ** n

    def test_processor(self):
        try:
            for _ in range(10):
                self.processorbound()
        except Exception as error:
            print("failed test processor bound: {}".format(error))


class TestMemory(unittest.TestCase):
    @benchtime.benchmethod
    def processormemorybound(self):
        "Processor memory bound concatinate 1KB strings into 1GB strings."
        # Create a 1KB test string of replicaions of the word SPAM for
        # simplicity
        y = SPAM_1KB * MB
        assert len(y) == GB

    def test_memory(self):
        try:
            for _ in range(10):
                self.processormemorybound()
        except Exception as error:
            print("failed test memory bound: {}".format(error))


class TestStorage(unittest.TestCase):
    @benchtime.benchmethod
    def storagebound(self):
        "Processor memory bound concatinate 1KB strings into files to create 1GB then read from file in chunks."
        # Create a 1KB test string of replicaions of the word SPAM for
        # simplicity
        len_x = len(SPAM_1KB)
        with open("tmp", "w") as f:
            for i in range(MB):
                f.write(SPAM_1KB)
        count = 0
        with open("tmp", "r") as f:
            while True:
                datachunk = f.read(len_x)
                if not datachunk:
                    break
                count += len(datachunk)
        assert count == GB

    def test_storage(self):
        try:
            for _ in range(10):
                self.storagebound()
        except Exception as error:
            print("failed test storage bound: {}".format(error))


if __name__ == "__main__":

    # Simple Argument check
    if (len(sys.argv) >= 2) and (sys.argv[1] == "run"):
        # print(benchtime.statistics)
        TestProcessorOperations().test_processor()
        TestMemory().test_memory()
        TestStorage().test_storage()
        benchtime.report()
        print("end")
    else:
        unittest.main()
