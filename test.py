def TwoSum(nums,target):
    
    for i in range(0,len):
        for j in range(i+1,len):
            if ( nums[i]+nums[j] == target ):
                return (print(i,j))

nums = []
target = int(input("Enter the TARGET : "))
len = int (input("Enter the length of the list: "))
for k in range (0,len):
    ele = int(input("Enter your Elements " +str([k])+": "))
    nums.append(ele)
TwoSum(nums,target)