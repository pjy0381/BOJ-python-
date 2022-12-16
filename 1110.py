n = input().rjust(2, "0")
a = []
while n not in a:
    a.append(n)
    s = str(int(n[0])+int(n[1])).rjust(2, "0")
    n = n[1] + s[1]
print(len(a))
