# https://zibada.guru/gcj/ks2016d/problems/#D


def dp(index, cur_min_l, cur_max_l, cur_cost, N, cost_cap, desired_l, A, B, P, inf_cost):
    if cur_cost > cost_cap:
        return inf_cost
    if desired_l < cur_min_l:
        return inf_cost
    if desired_l <= cur_max_l:
        return cur_cost
    if index == N:
        return inf_cost

    cost_skip = dp(index+1, cur_min_l, cur_max_l, cur_cost,
                   N, cost_cap, desired_l, A, B, P, inf_cost)
    cost_nonskip = dp(
        index+1, cur_min_l+A[index], cur_max_l+B[index], cur_cost+P[index], N, cost_cap, desired_l, A, B, P, inf_cost)
    return min(cost_nonskip, cost_skip)


T = int(input())
for t in range(1, T+1):
    N, M, L = map(int, input().split())
    P = []
    A = []
    B = []
    for n in range(N):
        a, b, p = map(int, input().split())
        P += p,
        A += a,
        B += b,
    MAXP = sum(P) + 1

    ans = dp(0, 0, 0, 0, N, M, L, A, B, P, MAXP)

    print('Case #%d: %s' % (t, str(ans) if ans != MAXP else 'IMPOSSIBLE'))
