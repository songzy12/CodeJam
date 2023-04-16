T = int(raw_input())
mod = 10**9+7

from collections import defaultdict
import string

for t in range(1, T+1):
    V, S = map(int, raw_input().split())

    def pos(c):
        return ord(c)-ord('a')

    def get_key(word):
        k = [0 for i in range(26)]
        for c in word:
            k[pos(c)] += 1
        return tuple(k)
    
    m = defaultdict(int)
    for v in range(V):
        word = raw_input()
        m[get_key(word)] += 1
    
    al = []
    def get_ans(sen):
        dp = [1] + [0 for i in range(len(sen))]
        
        for i in range(0, len(sen)):
            # i from 0 to len(sen) - 1
            k = [0 for _ in range(26)]
            for j in range(i, -1, -1):
                # consider the substr from j to i
                k[pos(sen[j])] += 1
                if tuple(k) in m:
                    dp[i+1] += dp[j] * m[tuple(k)]
                    dp[i+1] %= mod
        return dp[-1]
    
    for s in range(S):
        sen = raw_input()
        al += str(get_ans(sen)),
    print 'Case #%d: %s' % (t, ' '.join(al))
    
# use tuple as key, and do not count them repeatly
# count them iterately rather than use Counter
