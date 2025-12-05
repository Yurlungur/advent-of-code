#!/usr/bin/env python

from argparse import ArgumentParser

testdata = """3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""

def line_to_pair(line):
    ls,le = line.lstrip().rstrip().split('-')
    return [int(ls),int(le)]

def parse_input_string(s):
    rangelines,idlines = s.split('\n\n')
    ranges = [line_to_pair(l) for l in rangelines.split('\n')]
    ids = [int(l.lstrip().rstrip()) \
           for l in idlines.split('\n') if l.lstrip().rstrip()]
    return ranges,ids

def fuse_ranges(ranges):
    new_ranges = []
    for r in sorted(ranges, key = lambda x: x[0]):
        if len(new_ranges) > 0 and r[0] <= new_ranges[-1][1]:
            new_ranges[-1][1] = max(new_ranges[-1][1], r[1])
        else:
            new_ranges.append(r)
    return new_ranges

def in_valid_range(val, ranges):
    i = len(ranges)//2
    while True:
        if val < ranges[i][0]:
            if i <= 0 or val > ranges[i-1][1]:
                return False
            else:
                i = i // 2
        elif val > ranges[i][1]:
            if i >= len(ranges) - 1 or val < ranges[i+1][0]:
                return False
            else:
                i += (len(ranges) - i)//2
        else:
            return True

