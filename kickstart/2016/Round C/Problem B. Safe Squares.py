T = input()
for t in range(1, T+1):
    R, C, K = map(int, raw_input().split())
    # R, C \in [1, 3000], K \in  [0, 3000]
    grid = [[0 for i in range(C+1)] for j in range(R+1)]
    for i in range(R+1):
        grid[i][-1] = 1
    for j in range(C+1):
        grid[-1][j] = 1
    for j in range(K):
        r, c = map(int, raw_input().split())
        grid[r][c] = 1

    # the maximum possible side length as the left top corner
    dp = [[0 for i in range(C + 1)] for j in range(R + 1)] 
    
    for i in range(R, -1, -1):
        for j in range(C, -1, -1):
            if grid[i][j]:
                dp[i][j] = 0
            elif grid[i+1][j] or grid[i][j+1]:
                dp[i][j] = 1
            else:
                # notice the recursion formula
                dp[i][j] = min(dp[i+1][j+1], dp[i+1][j], dp[i][j+1]) + 1

    ans = 0
    for i in range(R+1):
        for j in range(C+1):
            ans += dp[i][j]
    print "Case #%d: %d" % (t, ans)

