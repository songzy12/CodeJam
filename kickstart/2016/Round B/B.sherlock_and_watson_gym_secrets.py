# https://zibada.guru/gcj/ks2016b/problems/#B

from collections import defaultdict


MOD = 10**9+7


def fast_pow(x, n, K):
    """Computes (x^n) % K using binary exponentiation."""
    res = 1
    while n:
        if n & 1:
            res = (res * x) % K
        x = (x * x) % K
        n >>= 1
    return res % K


def compute_mod_index_map(K, A):
    """Computes a map from (i^A % K) to list of indices i."""
    mod_index_map = defaultdict(list)
    for i in range(1, K+1):
        mod_index_map[fast_pow(i, A, K)].append(i)
    return mod_index_map


def compute_full_cycles(mod_index_a, mod_index_b, K, full_cycles):
    if full_cycles == 0:
        return 0

    total_pairs = 0
    for mod_a in mod_index_a:
        target_mod_b = (K - mod_a) % K
        if target_mod_b not in mod_index_b:
            continue

        for index_a in mod_index_a[mod_a]:
            total_pairs += len(mod_index_b[target_mod_b]) * full_cycles
            if index_a in mod_index_b[target_mod_b]:  # Requirement: i != j
                total_pairs -= 1
            total_pairs %= MOD
    return (total_pairs * full_cycles) % MOD


def compute_full_cycle_with_remainder(mod_index_a, mod_index_b, K, full_cycles, remainder):
    if full_cycles == 0 or remainder == 0:
        return 0

    total_pairs = 0
    for mod_a in mod_index_a:
        target_mod_b = (K - mod_a) % K
        if target_mod_b not in mod_index_b:
            continue

        for index_a in mod_index_a[mod_a]:
            count = 0
            for index_b in mod_index_b[target_mod_b]:
                if index_b > remainder:
                    break
                count += 1
            total_pairs += count * full_cycles
            total_pairs %= MOD
    return total_pairs % MOD


def compute_remainders(mod_index_a, mod_index_b, K, remainder):
    if remainder == 0:
        return 0

    total_pairs = 0
    for mod_a in mod_index_a:
        target_mod_b = (K - mod_a) % K
        if target_mod_b not in mod_index_b:
            continue

        for index_a in mod_index_a[mod_a]:
            if index_a > remainder:
                break
            for index_b in mod_index_b[target_mod_b]:
                if index_b > remainder:
                    break
                if index_a == index_b:
                    continue  # Requirement: i != j
                total_pairs += 1
    return total_pairs % MOD


def compute_pairs(mod_index_a, mod_index_b, K, N):
    full_cycles = (N // K) % MOD
    remainder = N % K
    return compute_full_cycles(mod_index_a, mod_index_b, K, full_cycles) + \
        compute_remainders(mod_index_a, mod_index_b, K, remainder) + \
        compute_full_cycle_with_remainder(mod_index_a, mod_index_b, K, full_cycles, remainder) + \
        compute_full_cycle_with_remainder(
            mod_index_b, mod_index_a, K, full_cycles, remainder)


def solve(K, A, B, N):
    mod_index_a = compute_mod_index_map(K, A)
    mod_index_b = compute_mod_index_map(K, B)
    # print(f"mod_index_a: {mod_index_a}")
    # print(f"mod_index_b: {mod_index_b}")
    return compute_pairs(mod_index_a, mod_index_b, K, N) % MOD


T = int(input())
for t in range(1, T+1):
    A, B, N, K = map(int, input().split())
    print(f"Case #{t}: {solve(K, A, B, N)}")
