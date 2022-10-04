def delete_nth(order,max_e):
    # code here
    result = []
    for photo in order:
        if photo not in result or result.count(photo) < max_e:
            result.append(photo)
    return result

print (delete_nth([1,1,3,3,7,2,2,2,2], 3))