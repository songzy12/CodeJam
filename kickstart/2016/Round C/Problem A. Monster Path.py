# dp

T = input()
for t in range(1, T+1):
    R, C, R_s, C_s, S = map(int, raw_input().split())
    P, Q = map(float, raw_input().split())
    grid = []
    count = [[0 for i in range(C)] for j in range(R)]
    for r in range(R):
        grid.append(map(lambda x: P if x == 'A' else Q, raw_input().split()))

    dirs = [(-1,0), (1,0), (0, 1), (0, -1)]
    ans = 0
    
    def solve(r, c, s):
        global ans
        if s < 0:
            return
        if s == 0:
            res = 0
            for r in range(R):
                for c in range(C):
                    res += 1 - (1 - grid[r][c]) ** count[r][c]
            ans = max(ans, res)
            return
            
        # this is not right: 
        # grid[r][c] = temp * (1 - temp)
        
        for i, j in dirs:
            r_, c_ = r + i, c + j
            if r_ < 0 or r_ >= R or c_ < 0 or c_ >= C:
                continue
            count[r_][c_] += 1 
            solve(r_, c_, s - 1)
            count[r_][c_] -= 1
        
    solve(R_s, C_s, S)
    print 'Case #%d: %.7f' % (t, ans)
    
# for a total count of n visit of a grid,
# number of monster caught is 1-(1-p)**n
# we can not compute this iterately