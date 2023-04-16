T = int(raw_input())
for t in range(1, T+1):
    N = int(raw_input())
    ans = 2
    def check(N, b):
        while N:
            N -= 1
            if N % b:
                return False
            N /= b
        return True
    while not check(N, ans):
        ans += 1
    print 'Case #%d: %d' % (t, ans)        

# pity: can check only whether N = (b^n-1) / (b-1)
# which is, N * (b-1) + 1 is power of b
