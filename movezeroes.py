# task: remove zeroes in a given list and add them to the end
def move_zeros(lst):
    # define a list for the zeroes to live in
    zeroes = []
    # repeat operation to remove 0s while there are any remaining
    while 0 in lst:
        lst.remove(0)
        # for each zero removed, add one to the zeroes list to reflect the count of removed integers
        zeroes.append(0)
    # finally, return the original list (now modified) with the zeroes list appended to the end
    return lst + zeroes

print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))