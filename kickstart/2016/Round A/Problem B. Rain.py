from sys import stdin

T = int(input())

def compute(t):
    R, C  = map(int, stdin.readline().strip().split())
    H = []
    for i in range(R):
        H += list(map(int, stdin.readline().strip().split())),

    W = [[1005 for j in range(C)] for i in range(R)]
    active = []
    for i in range(R):
        W[i][0] = H[i][0]
        W[i][C-1] = H[i][C-1]
        active += (i, 0),
        active += (i, C-1),
    for j in range(C):
        W[0][j] = H[0][j]
        W[R-1][j] = H[R-1][j]
        active += (0, j),
        active += (R-1, j),
    
    ds = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while active:
        r0, c0 = active.pop(0)
        for d in ds:
            r = r0 + d[0]
            c = c0 + d[1]
            if r < 0 or r == R or c < 0 or c == C:
                continue
            temp = min(W[r][c], max(H[r][c], W[r0][c0]))
            if W[r][c] != temp:
                W[r][c] = temp
                active += (r, c),
                
    #for row in W:
    #    print row

    ans = 0
    for i in range(R):
        for j in range(C):
            ans += W[i][j] - H[i][j]
    print "Case #%d: %d" % (t, ans)

for t in range(T):
    compute(t+1)
