sum = 0
a = 2;b=10



N = 10
x = int(input("Enter X"))
for i in range(1,N+1):
    sum = sum + a/b
    a += 1 ; b-= 1
print("sum of series =",sum)