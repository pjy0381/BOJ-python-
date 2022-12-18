a = [-1 for i in range(26)]
s = input()

for i in range(len(s)):
    c = s[i]
    if a[ord(c)-ord('a')] == -1:
        a[ord(c)-ord('a')] = i

print(" ".join(str(i) for i in a))        