#! /usr/bin/env python

import os
import sys

def test(programStr, inArr, outArr):
    outfile = open('test.cpp', 'w')
    testfile = open('testIn.txt', 'w')
    print >> outfile, programStr
    outfile.close()

    os.system("g++ test.cpp -o test")

    for i in range(len(inArr)):
        testfile.write(inArr(i));
        os.system("./test %s > testOut.txt", % (testfile))
        if !(areSame(outArr(i),"testOut.txt"):
            return "Failed..."

    return "Working"

def areSame(correct,testPath):
    

if __name__ == "__main__":
    inStr = sys.argv[1];
