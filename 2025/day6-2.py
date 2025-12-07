#!/usr/bin/env python

from argparse import ArgumentParser
import numpy as np

testdata = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +
"""

def do_math(s):
    lines = s.splitlines()
    ops = list(reversed(lines[-1].split()))
    args_arr = np.empty((len(lines), len(lines[0])), dtype="U1")
    for i, l in enumerate(lines[:-1]):
        args_arr[i] = list(l)
    args_arr = np.rot90(args_arr)

    # now  each row is a number to be operated on
    tot = 0
    iop = 0
    nums = []
    for ir, row in enumerate(args_arr):
        numstr = "".join([str(c) for c in row])
        if numstr.isspace():
            answer = np.sum(nums) if ops[iop] == '+' else np.prod(nums)
            print(ops[iop], nums, answer)
            tot += answer
            nums = []
            iop += 1
        else:
            nums.append(float(numstr))
    answer = np.sum(nums) if ops[iop] == '+' else np.prod(nums)
    print(ops[iop], nums, answer)
    tot += answer

    return tot

if __name__ == "__main__":    
    parser = ArgumentParser("do math")
    parser.add_argument("-f", "--filename", default=None, help="file to use")

    args = parser.parse_args()
    if args.filename is not None:
        with open(args.filename) as f:
            s = f.read()
    else:
        s = testdata

    print(do_math(s))
