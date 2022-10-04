def move_zeros(lst):
    zeroes = []
    result = lst
    while 0 in lst:
        lst.remove(0)
        zeroes.append(0)
    return lst + zeroes

print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))