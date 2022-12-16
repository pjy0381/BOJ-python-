a = []
for i in range(28):
    n = int(input())
    a.append(n)

for i in range(30):
    if i+1 not in a:
        print(i+1)
