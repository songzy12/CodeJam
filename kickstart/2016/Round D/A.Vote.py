# -*- coding: cp936 -*-
import operator  
def c(n,k):
    if k < 0:
        return 0
    return  reduce(operator.mul, range(n - k + 1, n + 1), 1) /reduce(operator.mul, range(1, k +1), 1) 

T = int(raw_input())
for t in range(1, T+1):
    N, M = map(int, raw_input().split())
    # ans = (c(M+N-1, N-1) - c(M+N-1, M-1)) * 1.0 / c(M+N,M)
    ans = (N - M) * 1.0 / (M + N)
    print 'Case #%d: %.8f' % (t, ans)

# http://m.blog.csdn.net/article/details?id=8722739