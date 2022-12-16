k = int(input())
for i in range(k):
    s = input()
    total = 0
    n = 0
    for j in range(len(s)):
        if (s[j] == "O"):
            n += 1
        else:
            n = 0
        total += n
    print(total)
