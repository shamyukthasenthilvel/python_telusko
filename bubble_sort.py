def sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                temp =nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp

nums=[8,6,5,1,2,0]
sort(nums)
print(nums)
