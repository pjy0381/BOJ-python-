a = int(input())
b = int(input())
c = a * b

for i in range(3):
    print(a*(b%10))
    b = b // 10
 
print(c)