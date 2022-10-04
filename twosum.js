const twoSum = function(nums, target) {
    const result = []
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] < target && nums.indexOf(target - nums[i]) != -1) {
            console.log(`pushing ${i} and ${nums.indexOf(target - nums[i])}`)
            result.push(i, nums.indexOf(target - nums[i]))
            break
        }
    }
    return result
};

console.log(twoSum([2,7,11,15], 9))