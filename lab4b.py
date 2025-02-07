#!/usr/bin/env python3

def join_lists(l1, l2):
    # Perform a union operation, convert back to list (without sorting)
    return list(set(l1) | set(l2))  

def match_lists(l1, l2):
    # Perform an intersection operation, convert back to list
    return list(set(l1) & set(l2))

def diff_lists(l1, l2):
    # Perform a symmetric difference operation, convert back to list
    return list(set(l1) ^ set(l2))

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [2, 1, 0, -1, -2]
    print('list1: ', list1)
    print('list2: ', list2)
    print('join: ', join_lists(list1, list2))
    print('match: ', match_lists(list1, list2))
    print('diff: ', diff_lists(list1, list2))

