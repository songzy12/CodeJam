# the value got by Newton method may not fall in the given region.

def f(r, m, c):
    ans = 0
    ans += -c[0]*(1+r)**m
    for i in range(1, m+1):
        ans += c[i]*(1+r)**(M-i)
    return ans

def df(r, m, c):
    ans = 0
    ans += -c[0]*m*(1+r)**(m-1)
    for i in range(1, m):
        ans += c[i]*(m-i)*(1+r)**(m-i-1)
    return ans

def it(x, m, c):
    return x-f(x, m, c)*1.0/df(x, m, c)
    
def compute(x, delta, m, c):
    xn = it(x, m, c)
    while abs(xn - x) > delta:
        x = xn
        xn = it(xn, m, c)
    return xn

T = int(input())
for t in range(T):
    M = int(input())
    from sys import stdin
    C = map(int, stdin.readline().strip().split())
    for x0 in [-1, 0, 1]:
        try:
            x = compute(x0, 10**(-9), M, C)
        except:
            continue
        if -1 < x < 1:
            break
    print "Case #%d: %.12f" % (t+1, x)

