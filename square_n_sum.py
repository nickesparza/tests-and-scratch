def square_sum(numbers):
    # loop over enumerated list to access the index and modify it
    for index, number in enumerate(numbers):
        # perform the square operation
        numbers[index] = number ** 2
        print(number)
    print(numbers)
    # use the built-in sum function to return the sum of all list elements
    return sum(numbers)

print(square_sum([0, 3, 4, 5]))