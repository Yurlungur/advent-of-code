#!/usr/bin/env python

from argparse import ArgumentParser

testdata=""".......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
"""

def parse_string(s):
    data = set()
    lines = s.splitlines()
    numrows = len(lines)
    numcols = len(lines[0])
    js = 0
    for i,row in enumerate(lines):
        for j,char in enumerate(list(row)):
            if char == 'S':
                js = j
            if char == '^':
                data.add((i, j))
    return numrows, numcols, js, data

def count_splits(i, j, touchedset, numrows, data):
    "Count the number of splits by depth-first search"
    # This check makes it bfs-adjacent. Only touch a splitter once.
    if i >= numrows or (i,j) in touchedset:
        return 0
    if (i, j) in data:
        touchedset.add((i, j))
        return count_splits(i, j-1, touchedset, numrows, data) + count_splits(i, j+1, touchedset, numrows, data) + 1
    else:
        return count_splits(i+1, j, touchedset, numrows, data)

def count_paths(js, numrows, numcols, data):
    "Now we just walk down rows"
    import numpy as np
    # 1 col on each side of guard cells
    NG=1
    active_count = np.zeros((numrows + 2*NG),dtype=int)
    active_count[js+NG] = 1
    for i in range(numrows):
        active_count_next = np.zeros_like(active_count)
        for j in range(numcols):
            if active_count[j+NG]:
                if (i, j) in data:
                    active_count_next[j+NG-1] += active_count[j+NG]
                    active_count_next[j+NG+1] += active_count[j+NG]
                else:
                    active_count_next[j+NG] += active_count[j+NG]
        active_count = active_count_next

    return active_count.sum()

if __name__ == "__main__":    
    parser = ArgumentParser("Get tachyon manifod")
    parser.add_argument("-f", "--filename", default=None, help="file to use")
    parser.add_argument("-p", "--part2", action="store_true", help="run part 2")

    args = parser.parse_args()

    if args.filename is not None:
        with open(args.filename) as f:
            numrows, numcols, js, data = parse_string(f.read())
    else:
        numrows, numcols, js, data = parse_string(testdata)
    if args.part2:
        path_cache = set()
        completed_paths = set()
        currpath = ((0, js),)
        print(count_paths(js, numrows, numcols, data))
    else:
        touchedset = set()
        print(count_splits(0, js, touchedset, numrows, data))
