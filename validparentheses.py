def isValid(s: str) -> bool:
    stack = []
    
    for val in s:
        if val in '{[(':
            stack.append(val)
        else:
            if not stack or stack.pop() + val not in ['[]', '{}', '()']:
                return False
    
    if stack:
        return False
    else:
        return True

print(isValid("([)]"))