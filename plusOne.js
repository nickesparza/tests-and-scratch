var plusOne = function(digits) {
    if (digits[digits.length - 1] != 9) {
        // console.log('a normal thing')
        digits[digits.length - 1]++
        return digits
    }
    if (digits.every(num => num === 9)) {
        // console.log("they're all 9s")
        const result = digits.map(number => number = 0)
        result[0] = 1
        result.push(0)
        return result
    }
    if (digits[digits.length - 1] === 9) {
        // console.log('oh god')
        let inc = digits.length - 1
        while (digits[inc] === 9) {
            inc--
        }
        // console.log('this is inc', inc)
        // console.log('this is the number at index inc', digits[inc])
        // console.log('this is the number at index inc - 1', digits[inc - 1])
        digits[inc]++
        for (let i = inc + 1; i < digits.length; i++) {
            digits[i] = 0
        }
        return digits
    }
};

console.log(plusOne([6,1,4,5,3,9,0,1,9,5,1,8,6,7,0,5,5,4,3]))
console.log(plusOne([9,9,9,9,9,9]))
console.log(plusOne([9]))
console.log(plusOne([1,2,3,4,5,9,9,9,9,9,9,9]))