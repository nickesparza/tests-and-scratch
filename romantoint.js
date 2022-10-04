const romanToInt = function(s) {
    // split the string into an array
    // convert each numeral into its corresponding number
    // iterate through array
    // take the current number, add the next number to it
    // UNLESS the current number is less than the next number
    // in that case, subtract the current number from the next number
    const splitNumeral = s.split("")
    const numConvert = splitNumeral.map(numeral => {
        switch(numeral) {
            case "I":
                return 1
            case "V":
                return 5
            case "X":
                return 10
            case "L":
                return 50
            case "C":
                return 100
            case "D":
                return 500
            case "M":
                return 1000
        }
    })
    let sum = 0
    numConvert.forEach((number, index) => {
        if (number < numConvert[index + 1]) {
            sum -= number
        } else {
            sum += number
        }
    })
    return sum
};

console.log(romanToInt("MDLCIII"))