a = []
for i in range(10000):
    t = i
    for j in str(i):
        t+=int(j)
    a.append(t)
    if i not in a :
        print(i)
