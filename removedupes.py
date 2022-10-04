# task: remove duplicates in a sorted array
def removeDuplicates(nums):
    for num in nums:
        # leverage the list function 'count' to establish condition for while loop
        while nums.count(num) > 1:
            # while there are any more than one of a given number in the list, remove that number
            # because the list is sorted, no need for further specificity
            nums.remove(num)
    return nums

print(removeDuplicates([1,1,1,1,2,3,4,4,4,5,6,7]))