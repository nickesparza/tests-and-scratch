# determine if a string of parens is valid
def isValid(s: str) -> bool:
    # define a list to add/remove parens during operation
    stack = []
    for val in s:
        # if the value is an open paren, add it to the stack
        if val in '{[(':
            stack.append(val)
        # else (meaning it is a closed paren)
        else:
            # if the last character doesn't match with the current character as a pair
            if not stack or stack.pop() + val not in ['[]', '{}', '()']:
                return False
    # if there is anything left in the stack at the end, there was an odd number of parens
    if stack:
        return False
    else:
        return True

print(isValid("([)]"))