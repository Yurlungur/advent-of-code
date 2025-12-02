from argparse import ArgumentParser

ranges={'true' : "9100-11052,895949-1034027,4408053-4520964,530773-628469,4677-6133,2204535-2244247,55-75,77-96,6855-8537,55102372-55256189,282-399,228723-269241,5874512-6044824,288158-371813,719-924,1-13,496-645,8989806846-8989985017,39376-48796,1581-1964,699387-735189,85832568-85919290,6758902779-6759025318,198-254,1357490-1400527,93895907-94024162,21-34,81399-109054,110780-153182,1452135-1601808,422024-470134,374195-402045,58702-79922,1002-1437,742477-817193,879818128-879948512,407-480,168586-222531,116-152,35-54",
        'test' : "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"}

def is_invalid_part1(key):
    # Odd-length keys cannot be invalid
    l = len(key)
    if len(key) % 2:
        return False
    return key[:l//2] == key[l//2:]

def check_is_repeat(key, pattern):
    if len(key) % len(pattern) != 0:
        return False
    multiplicity = len(key) // len(pattern)
    for i in range(0, multiplicity):
        if key[i*len(pattern):(i+1)*len(pattern)] != pattern:
            return False
    return True

def is_invalid_part2(key):
    if len(key) == 0:
        return False
    for i in range(1,len(key)//2+1):
        seq = key[:i]
        if check_is_repeat(key, seq):
            return True
    return False

def sum_invalid_keys(range_string,
                     is_invalid = is_invalid_part1,
                     debug = False):
    s = 0 # sum of invalid keys
    ranges = range_string.split(',')
    for r in ranges:
        boundstrs = r.split('-')
        startint,endint = (int(b) for b in boundstrs)
        for i in range(startint, endint+1):
            if is_invalid(f"{i}"):
                if debug:
                    print(f"Invalid key in range {r} is {i}")
                s = s + i

    return s

if __name__ == "__main__":
    parser = ArgumentParser("Get invalid keys")
    parser.add_argument("-t", "--test", action="store_true",
                        help="If we're using the test input")
    parser.add_argument("-d", "--debug", action="store_true",
                        help="Add debug messages")
    parser.add_argument("-p", "--part2", action="store_true",
                        help="Part 2")
    args = parser.parse_args()
    tester = is_invalid_part2 if args.part2 else is_invalid_part1
    if args.test:
        print(sum_invalid_keys(ranges['test'], tester, args.debug))
    else:
        print(sum_invalid_keys(ranges['true'], tester, args.debug))
