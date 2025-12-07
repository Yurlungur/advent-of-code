#!/usr/bin/env python

from argparse import ArgumentParser
import numpy as np

testdata = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +
"""

def parse_string(s):
    lines = s.splitlines()
    ops = lines[-1].split()
    args = np.empty((len(lines)-1, len(ops)),dtype=int)
    for i,l in enumerate(lines[:-1]):
        args[i,:] = np.fromstring(l, sep=' ', dtype=int)
    return args, ops

def parse_file(filename):
    with open(filename) as f:
        return parse_string(f.read())

def compute_op(args, ops):
    results = np.empty((len(ops)), dtype=int)
    for i, op in enumerate(ops):
        results[i] = args[:,i].sum() if op == '+' else args[:,i].prod()
    return results

if __name__ == "__main__":    
    parser = ArgumentParser("Do math")
    parser.add_argument("-f", "--filename", default=None, help="file to use")

    args = parser.parse_args()
    if args.filename is not None:
        vals, ops = parse_file(args.filename)
    else:
        vals, ops = parse_string(testdata)
    print(compute_op(vals, ops).sum())
