term = input("Enter the Term: ")
x = 0
y = 1
z = 0
term = int(term)
while z <= term:
    print(z)
    x = y
    y = z
    z = x + y

