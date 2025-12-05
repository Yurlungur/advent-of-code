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

def parse_input_file(filename):
    with open(filename) as f:
        return parse_input_string(f.read())

def fuse_ranges(ranges):
    """Take possibly overlapping ranges and build sorted set
    of non-verlapping ones by fusing the ones that overlap"""
    new_ranges = []
    for r in sorted(ranges, key = lambda x: x[0]):
        if len(new_ranges) > 0 and r[0] <= new_ranges[-1][1]:
            new_ranges[-1][1] = max(new_ranges[-1][1], r[1])
        else:
            new_ranges.append(r)
    return new_ranges

def in_valid_range(ranges, val):
    "Binary search over ranges to find the range containing value, if it exists"
    L = 0
    R = len(ranges) - 1
    while True:
        m = L + (R - L) // 2
        if val < ranges[m][0]:
            if m <= 0 or val > ranges[m-1][1]:
                return False
            else:
                R = m - 1
        elif val > ranges[m][1]:
            if m >= len(ranges) - 1 or val < ranges[m+1][0]:
                return False
            else:
                L = m + 1
        else:
            return True

def count_valid(ranges, ids):
    num_valid = 0
    for val in ids:
        num_valid += in_valid_range(ranges, val)
    return num_valid

def count_possibly_valid(ranges):
    tot = 0
    for r in ranges:
        tot += r[1] - r[0] + 1
    return tot

if __name__ == "__main__":    
    parser = ArgumentParser("Get accessible paper rolls")
    parser.add_argument("-f", "--filename", default=None, help="file to use")
    parser.add_argument("-p", "--part2", action="store_true", help="run part 2")

    args = parser.parse_args()

    if args.filename is not None:
        ranges,ids = parse_input_file(args.filename)
    else:
        ranges,ids = parse_input_string(testdata)
    ranges = fuse_ranges(ranges)
    if args.part2:
        print(count_possibly_valid(ranges))
    else:
        print(count_valid(ranges, ids))
