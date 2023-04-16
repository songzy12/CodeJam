T = int(raw_input())
for t in range(1, T+1):
    N = int(raw_input())
    R = map(int, raw_input().split())
    B = map(int, raw_input().split())

    def compute(perm):
        res = 0
        droped = [False for i in range(N)]
        for num in perm[:-1]:
            temp = 1 << 32

            for i in range(N):
                if i == num or droped[i]:
                    continue
                temp = min([temp, B[num] ^ R[i], R[num] ^ B[i]])
            
            res += temp
            droped[num] = True
        return res
        

    ans = 1 << 32

    from itertools import permutations
    for perm in permutations(range(N)):
        temp = compute(perm)
        if temp < ans:
            ans = temp

    print "Case #%d: %d" % (t, ans)
 
