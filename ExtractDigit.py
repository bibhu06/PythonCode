a = int (input("Enter the Number : "))
b =[]
while (a > 0):
    c = a % 10
    b.append(c)
    a = a // 10

print(b)
