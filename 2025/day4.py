#!/usr/bin/env python

from argparse import ArgumentParser
import numpy as np

testdata="""..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""

def string_to_padded_array(s):
    stringrows = s.lstrip().rstrip().replace('.','0').replace('@','1').split()
    nrow = len(stringrows)
    ncol = len(stringrows[0])
    array = np.zeros((nrow + 2, ncol + 2), dtype=int)
    for i,r in enumerate(stringrows):
        for j,c in enumerate(r):
            array[i+1, j+1] = int(c)
    return array

def file_to_padded_array(filename):
    with open(filename) as f:
        string = f.read()
    return string_to_padded_array(string)

def get_neighbor_counts(a):
    neighbors = np.zeros((8, a.shape[0], a.shape[1]), dtype=int)
    neighbors[0,1:,:] = a[:-1,:] # up
    neighbors[1,:-1,:] = a[1:,:] # down
    neighbors[2,:,1:] = a[:,:-1] # left
    neighbors[3,:,:-1] = a[:,1:] # right
    neighbors[4,:-1,:-1] = a[1:,1:] # up right
    neighbors[5,1:,1:] = a[:-1,:-1] # down left
    neighbors[6,1:,:-1] = a[:-1,1:] # down right
    neighbors[7,:-1,1:] = a[1:,:-1] # up left
    # only trustworthy in interior, not padded region
    return neighbors.sum(axis=0)

def get_accessible(a):
    counts = get_neighbor_counts(a)
    return np.logical_and(a[1:-1, 1:-1], counts[1:-1,1:-1] < 4).astype(int)

def count_accessible(a):
    return get_accessible(a).sum()

def count_removable(a):
    sum_removed = 0
    more_accessible = True
    while True:
        accessible = get_accessible(a)        
        num_accessible = accessible.sum()
        if num_accessible <= 0:
            break
        a[1:-1,1:-1][accessible > 0] = 0
        sum_removed += num_accessible
    return sum_removed

if __name__ == "__main__":    
    parser = ArgumentParser("Get accessible paper rolls")
    parser.add_argument("-f", "--filename", default=None, help="file to use")
    parser.add_argument("-p", "--part2", action="store_true", help="run part 2")

    args = parser.parse_args()
    a = None
    if args.filename is not None:
        a = file_to_padded_array(args.filename)
    else:
        a = string_to_padded_array(testdata)
    if args.part2:
        print(count_removable(a))
    else:
        print(count_accessible(a))
