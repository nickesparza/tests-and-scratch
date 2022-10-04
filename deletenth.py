# given a list where each integer represents a photo in a specific genre
# and a second integer representing the maximum number of times that genre can exist in the list
# return a list in the same order where any given integer does not exceed the maximum number defined by max_e
def delete_nth(order,max_e):
    # define a list to hold the result
    result = []
    for photo in order:
        # if the photo is not in the result list (count is 0) OR the count of photos is less than max_e, append to the result list
        # otherwise, do nothing. this preserves the original order
        if photo not in result or result.count(photo) < max_e:
            result.append(photo)
    return result

print(delete_nth([1,1,3,3,7,2,2,2,2], 3))