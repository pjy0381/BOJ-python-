n = int(input())
for i in range(n) :
    num,s = input().split()
    a = ''
    for j in s :
        a+=j*int(num)
    print(a)
