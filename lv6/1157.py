from string import ascii_uppercase

d = {}

for i in ascii_uppercase:
    d[i] = 0

s = input()
s = s.upper()

for i in s:
    d[i]+=1

tmp = [k for k,v in d.items() if max(d.values()) == v]

if len(tmp)>1 : print("?")
else : print(tmp[0])