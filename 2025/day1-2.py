#!/usr/bin/env python

from argparse import ArgumentParser

class Safe:
    def __init__(self, start = 0, mod = 100):
        self.loc = start
        self.mod = mod
        self.zero_count = 0
        self.zero_count_inflight = 0
    def update(self, s, debug = False):
        dir = -1 if s[0] == 'L' else 1
        mag = abs(int(eval(s[1:])))
        delta = dir * (mag % self.mod)
        new_loc = (self.loc + delta) % self.mod
        if new_loc == 0:
            self.zero_count = self.zero_count + 1
        rotations = mag // self.mod
        sign_crossing = self.loc != 0 and (new_loc == 0 or (((self.loc + delta) > self.mod) or ((self.loc + delta) < 0)))
        self.zero_count_inflight = self.zero_count_inflight + sign_crossing + rotations
        self.loc = new_loc
        if debug:
            print("s, loc, count_end, count_inf = {}, {}, {}, {}".format(s,
                                                                         self.loc,
                                                                         self.zero_count,
                                                                         self.zero_count_inflight))
    def update_from_sequence(self, seq, debug = False):
        for s in seq:
            self.update(s.lstrip().rstrip(), debug)
    def update_from_file(self, filename, debug = False):
        with open(filename) as f:
            self.update_from_sequence(f.readlines(), debug)

if __name__ == "__main__":
    parser = ArgumentParser("Advent of code day 1, part 1. safe problem")
    parser.add_argument("filename",
                        type=str,
                        help="file to read for sequence")
    parser.add_argument("--start", default = 50,
                        help="starting location of the dial")
    parser.add_argument("-t", "--test", action="store_true",
                        help="If we're using the test input")
    parser.add_argument("-d", "--debug", action="store_true",
                        help="Add debug messages")
    args = parser.parse_args()
    s = Safe(args.start)
    if args.test:
        s.update_from_sequence([
            "L68"
            , "L30"
            , "R48"
            , "L5"
            , "R60"
            , "L55"
            , "L1"
            , "L99"
            , "R14"
            , "L82"
        ], args.debug)
    else:
        s.update_from_file(args.filename, args.debug)
    print(s.zero_count, s.zero_count_inflight)

