T = int(raw_input())
for t in range(1, T+1):
    N, M = map(int, raw_input().split())
    row = map(int, raw_input().split())

    ans = 0

    def compute(perm):
        res = 0
        cut = [False for i in range(M)]

        def prize(pos):
            p = row[pos]
            i = pos + 1
            while i < M and not cut[i - 1]:
                if row[i] < p:
                    p = row[i]
                i += 1
            i = pos - 1
            while i >= 0 and not cut[i]:
                if row[i] < p:
                    p = row[i]
                i -= 1
            return p
        
        for pos in perm:
            temp = prize(pos)
            cut[pos] = True
            res += temp

        return res
    
    from itertools import permutations
 
    for perm in permutations(range(M - 1)):
        temp = compute(perm)
        # print perm, temp
        if temp > ans:
            ans = temp

    print "Case #%d: %d" % (t, ans)
        
   
    
