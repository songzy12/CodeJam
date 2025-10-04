# https://zibada.guru/gcj/ks2016a/problems/#A

from sys import stdin

import functools


def count_distinct_chars(name):
    return len(set(name.replace(' ', '')))


def compare_name(name1, name2):
    # First by distinct char count (descending)
    c1 = count_distinct_chars(name1)
    c2 = count_distinct_chars(name2)
    if c1 != c2:
        return -1 if c1 > c2 else 1
    # Then by lexicographical order (ascending)
    return -1 if name1 < name2 else 1


def compute_leader(names):
    names.sort(key=functools.cmp_to_key(compare_name))
    return names[0]


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    names = []
    for i in range(N):
        name = stdin.readline().strip()
        names.append(name)
    print(f"Case #{t}: {compute_leader(names)}")
