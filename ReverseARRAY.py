arr = []
n = int(input("Enter the LENGTH of ARRAY : "))
for i in range (0,n) :
    elem = input("Enter the ELEMENT : ")
    arr.append(elem)
print("The ARRAY is : "+str(arr))
print("The Reversed ARRAY is : "+str(arr[::-1]))