# first of all, remove all the space in the input

from sys import stdin
T = int(input())
for t in range(1, T+1):
    ans = ''
    N = int(input())
    names = []
    for i in range(N):
        temp = stdin.readline().strip()
        names += temp,
    names = map(lambda x: (-len(set(x.replace(' ', ''))), x), names)
    names.sort()
    print 'Case #%d: %s' % (t, names[0][-1])
        
