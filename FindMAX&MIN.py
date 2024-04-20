arr = []
n = int(input("Enter the LENGTH of ARRAY : "))
for i in range(0,n) :
    elem = int(input("Enter the ELEMENTS : "))
    arr.append(elem)
print("The ARRAY is : "+str(arr))
max = arr[0]
min = arr[1]
for i in range(0,len(arr)) :
    if  (arr[i] > max) :
        max = arr[i]
for i in range(0,len(arr)) :
    if  (arr[i] < min) :
        min =  arr[i]
print("The MAXIMUM ELEMENT is : "+str(max))
print("The MINIMUM ELEMENT is : "+str(min))