"""def find_missing_number(nums):
    n=len(nums)
    for i in range(n):
        for j in range(0,n-i-1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
    return nums

print(find_missing_number([1,7,3,5]))"""

