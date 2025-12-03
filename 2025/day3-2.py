#!/usr/bin/env python
test_data = "987654321111111,811111111111119,234234234234278,818181911112111"

from argparse import ArgumentParser

def argmax(seq):
    "input: a sequence of chars interpeted as ints"
    return max(enumerate(seq), key=lambda x: int(x[1]))[0]

def max_digit(seq, l):
    "Get the max digit in the sequence, excluding the last l digits"
    idx = argmax(seq[:-l]) if l > 0 else argmax(seq)
    val = seq[idx]
    return idx, val

def max_pair(seq):
    "input: a sequence of chars interpeted as ints"
    ndigits = 2
    # because it can't be the last element
    first_idx, first_max = max_digit(seq, ndigits - 1)
    # because it can't be the same as the first digit
    second_max = max(seq[first_idx+1:]) 
    # assumes string concat
    combined = str(first_max) + str(second_max)
    print(combined)
    return int(combined)

def max_ordered_subset(seq):
    ndigits = 12

    vals = []
    while ndigits > 0:
        idx, val = max_digit(seq, ndigits - 1)
        vals.append(val)
        seq = seq[idx+1:]
        ndigits -= 1
    number = "".join(vals)
    return int(number)

def sum_seqs(seqs, get_max):
    return sum([get_max(seq.lstrip().rstrip()) for seq in seqs])

if __name__ == "__main__":    
    parser = ArgumentParser("Get sum of max 2-digit number pair in sequences")
    parser.add_argument("-f", "--filename", default=None, help="file to use")
    parser.add_argument("-p", "--part2", action="store_true", help="run part 2")

    args = parser.parse_args()
    mode = max_ordered_subset if args.part2 else max_pair
    if args.filename is not None:
        with open(args.filename) as f:
            print(sum_seqs(f.readlines(), mode))
    else:
        print(sum_seqs(test_data.split(','), mode))

    
