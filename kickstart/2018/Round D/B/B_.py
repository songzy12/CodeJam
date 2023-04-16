
T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    p1, p2, a1, b1, c1, m1 = map(int, input().split())
    h1, h2, a2, b2, c2, m2 = map(int, input().split())
    x1, x2, a3, b3, c3, m3 = map(int, input().split())
    y1, y2, a4, b4, c4, m4 = map(int, input().split())

    p = []
    h = []
    x = []
    y = []

    for i in range(N):
        p.append(p1)
        temp = ((a1 * p2 + b1 * p1 + c1) % m1) + 1
        p1 = p2
        p2 = temp
    for i in range(N):
        h.append(h1)
        temp = ((a2 * h2 + b2 * h1 + c2) % m2) + 1
        h1 = h2
        h2 = temp
    for i in range(K):
        x.append(x1)
        temp = ((a3 * x2 + b3 * x1 + c3) % m3) + 1
        x1 = x2
        x2 = temp
    for i in range(K):
        y.append(y1)
        temp = ((a4 * y2 + b4 * y1 + c4) % m4) + 1
        y1 = y2
        y2 = temp

    cnt = 0
    for i in range(K):
        # h - p >= y - x and x <= p
        # or (x >= p) and h + p >= y + x
        for j in range(N):
            if (x[i] >= p[j] and h[j] + p[j] >= y[i] + x[i]) or \
                    (x[i] < p[j] and h[j] - p[j] >= y[i] - x[i]):
                cnt += 1
                break
    print("Case #%d: %d" % (t, cnt))
