T = int(input())
for t in range(1, T + 1):
    N, O, D = map(int, input().split())
    X1, X2, A, B, C, M, L = map(int, input().split())

    def solve(N, O, D, X1, X2, A, B, C, M, L):
        prefix = [0 for i in range(N + 1)]
        cnt_odd = [0 for i in range(N + 1)]

        for i in range(N):
            prefix[i + 1] = prefix[i] + X1 + L
            cnt_odd[i + 1] = cnt_odd[i] + ((X1 + L) % 2)
            temp = (A * X2 + B * X1 + C) % M
            X1 = X2
            X2 = temp

        ans = None
        for head in range(N):
            for tail in range(head + 1, N + 1):
                if cnt_odd[tail] - cnt_odd[head] <= O and \
                        prefix[tail] - prefix[head] <= D:
                    if not ans:
                        ans = prefix[tail] - prefix[head]
                    else:
                        ans = max(ans, prefix[tail] - prefix[head])

        return str(ans) if ans != None else "IMPOSSIBLE"

    print("Case #%d: %s" % (t, solve(N, O, D, X1, X2, A, B, C, M, L)))
