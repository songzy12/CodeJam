# https://zibada.guru/gcj/ks2016d/problems/#D
#
# https://codeforces.com/blog/entry/47796
#
# Main: DP
#   Let dp[n][L] = the least money to create a rope of exactly size L, using the first n ropes.
#   Then dp[n][L] = min(dp[n-1][L], min_{a <= t <= b} dp[n-1][t] + p)
# Time complexity: O(N * L^2)
#
# Reduce the time complexity to O(N * L) by
#   using dequeue to maintain the minimum value of dp[n-1][t] + p for t in [L-b, L-a].


from dataclasses import dataclass
from math import inf
from typing import List


@dataclass
class ProblemData:
    N: int  # Number of ropes
    M: int  # Maximum money available
    L: int  # Target length to reach or exceed
    A: List[int]  # Minimum length of each rope
    B: List[int]  # Maximum length of each rope
    P: List[int]  # Cost of each rope


def solve(data: ProblemData):
    # Let dp[n][L] = the least money to create a rope of exactly size L, using the first n ropes.
    dp = [[inf] * (data.L + 1) for _ in range(data.N + 1)]

    dp[0][0] = 0
    for n in range(1, data.N + 1):
        a = data.A[n-1]
        b = data.B[n-1]
        p = data.P[n-1]
        for l in range(data.L + 1):
            dp[n][l] = min(dp[n][l], dp[n-1][l])
            for t in range(max(0, l - b), l - a + 1):
                dp[n][l] = min(dp[n][l], dp[n-1][t] + p)
    return dp[data.N][data.L]


T = int(input())
for t in range(1, T+1):
    N, M, L = map(int, input().split())
    A = []
    B = []
    P = []
    for n in range(N):
        a, b, p = map(int, input().split())
        A += a,
        B += b,
        P += p,

    data = ProblemData(N, M, L, A, B, P)
    ans = solve(data)

    print('Case #%d: %s' % (t, str(ans) if ans <= data.M else 'IMPOSSIBLE'))
