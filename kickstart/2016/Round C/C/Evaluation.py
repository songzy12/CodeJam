from collections import defaultdict

T = int(raw_input())

for t in range(1, T+1):
    m = defaultdict(list)
    count = defaultdict(int)
    N = int(raw_input())
    for n in range(N):
        exp = raw_input()
        v, r = exp.split('=')
        l = r.split('(')[-1].split(')')[0].split(',')
        if not l or not l[0]:
            count[v] = 0
            continue
        count[v] += len(l)
        for x in l:
            m[x].append(v)
    while 0 in count.values():
        for key, value in count.items():
            if value == 0:
                for x in m[key]:
                    count[x] -= 1
                count.pop(key)
    print 'Case #%d: %s' % (t, 'GOOD' if len
                            (count) == 0 else 'BAD')
