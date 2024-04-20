a = int(input("Enter your 1st number : "))
b = int(input("Enter your 2nd number : "))
print("Before Swapping a = "+str(a)+" and b = "+str(b))
a = a + b
b = a - b
a = a - b
print("After Swapping a = "+str(a)+" and b = "+str(b))