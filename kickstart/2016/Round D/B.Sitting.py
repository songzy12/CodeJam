T = int(raw_input())
for t in range(1, T+1):
    def compute(row, col):
        if col <= 0:
            return 0
        if r <= 2:
            return r * (c - c / 3)
        return r * c - r * c / 3
        
    r, c = map(int, raw_input().split())
    if r > c:
        r, c = c, r # this is important!!!
    ans = compute(r, c)
    
    print 'Case #%d: %d' % (t, ans)

'''
xox xox xox ...
xxo xxo xxo ...
oxx oxx oxx ...
... ... ... ...
'''