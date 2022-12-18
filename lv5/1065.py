n = int(input())

def solution(n):
    if n<100:
        return n

    t = 99
    for i in range(100,n+1):
        s = str(i)
        if int(s[0]) - int(s[1]) == int(s[1]) - int(s[2]):
            t+=1
    return t

print(solution(n))
