def square_sum(numbers):
    #your code here
    for index, number in enumerate(numbers):
        numbers[index] = number ** 2
        print(number)
    print(numbers)
    return sum(numbers)

print(square_sum([0, 3, 4, 5]))