T = int(raw_input())
for t in range(1, T+1):
    def compute(n, p):
        if n % p:
            return n / p, n % p
        return n / p - 1, p
            
    S = raw_input()
    I, J = map(int, raw_input().split())
    L = len(S)
    ni, i = compute(I, L)
    nj, j = compute(J, L)
    ans = S.count('B') * nj + S[:j].count('B')
    ans -= S.count('B') * ni + S[:i-1].count('B')
    print 'Case #%d: %d' % (t, ans)
