# https://zibada.guru/gcj/ks2016a/problems/#A

from sys import stdin


def count_distinct_chars(name):
    return len(set(name.replace(' ', '')))


def compute_leader(names):
    # First by distinct char count (descending)
    # Then by lexicographical order (ascending)
    names.sort(key=lambda name: (-count_distinct_chars(name), name))
    return names[0]


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    names = []
    for i in range(N):
        name = stdin.readline().strip()
        names.append(name)
    print(f"Case #{t}: {compute_leader(names)}")
