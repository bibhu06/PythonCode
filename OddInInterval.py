low = int(input("Enter the Start of Range : "))
high = int(input("Enter the End of Range : "))
count = 0
for i in range(low,high + 1):
    if (i % 2 != 0):
        count = count + 1
print(count)