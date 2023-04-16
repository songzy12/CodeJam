T = int(raw_input())
for t in range(1, T+1):
    N, M, L = map(int, raw_input().split())
    P = []
    A = []
    B = []
    for n in range(N):
        a, b, p = map(int, raw_input().split())
        P += p,
        A += a,
        B += b,
    MAXP = sum(P) + 1
    def dp(index, left, right, value):
        if value > M:
            return MAXP
        if left > L:
            return MAXP
        if L <= right:
            return MAXP
        if index == N:
            return MAXP
        return min(dp(index+1, left+A[index], right+B[index], value+P[index]),
                   dp(index+1, left, right, value))
    
    '''
    def compute():
        cost = sum(P) + 1
        for state in range(2**N):
            def get(state):
                a, b, c = 0, 0, 0
                i = 0
                while state:
                    if state & 1:
                        a += A[i]
                        b += B[i]
                        c += P[i]
                    state >>= 1
                    i += 1
                return a, b, c
            
            a, b, c = get(state)
            if c <= M and a <= L <= b and c < cost:
                cost = c
        return cost
    ans = compute()
    '''
        
    ans = dp(0, 0, 0, 0)
    print 'Case #%d: %s' % (t, str(ans) if ans != MAXP else 'IMPOSSIBLE')
