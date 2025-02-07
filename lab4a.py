#!/usr/bin/env python3

def join_sets(s1, s2):
    # Return a set containing all values from both sets
    return s1 | s2  # or s1.union(s2)

def match_sets(s1, s2):
    # Return a set containing values that appear in both sets
    return s1 & s2  # or s1.intersection(s2)

def diff_sets(s1, s2):
    # Return a set containing values that are in either set, but not both
    return s1 ^ s2  # or s1.symmetric_difference(s2)

if __name__ == '__main__':
    set1 = set(range(1,10))
    set2 = set(range(5,15))
    print('set1: ', set1)
    print('set2: ', set2)
    print('join: ', join_sets(set1, set2))
    print('match: ', match_sets(set1, set2))
    print('diff: ', diff_sets(set1, set2))

