list = []
len = int(input("Enter the Length of ARRAY : "))
for i in range (0,len):
    ele = int(input("Enter the Element " + str(i) +" : "))
    list.append(ele)
print(list)
rot = int(input("Enter the rotation index : "))
rotated_list = list[rot:] + list[:rot]
print(rotated_list)