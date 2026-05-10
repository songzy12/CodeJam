T = int(raw_input())
for t in range(1, T+1):
    N, D = map(int, raw_input().split())
    def compute(N, d):
    # the first is d
        ans = 0
        for x in range(1, N / d + 1):
            y = N - x * d
            def compute0(x, y):
                a = max(x-y, 1)
                b = min((2*x-y)/2, x)
                if a > b:
                    return 0
                return b - a + 1
            ans += compute0(x, y) 
        return ans
    ans = 0
    for d in range(D, N+1, D):
        ans += compute(N, d)
    print 'Case #%d: %d' % (t, ans)
