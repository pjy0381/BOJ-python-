N, X = map(int, input().split())
a = list(map(int, input().split()))
r = []
for i in range(N):
    if (a[i] < X):
        r.append(a[i])

print(' '.join(str(s) for s in r))
