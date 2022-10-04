def removeDuplicates(nums):
    for num in nums:
        while nums.count(num) > 1:
            nums.remove(num)
    return nums

print(removeDuplicates([1,1,1,1,2,3,4,4,4,5,6,7]))