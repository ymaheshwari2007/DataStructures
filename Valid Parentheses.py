def isValid(s: str) -> bool:
    op = {")":"(", "]":"[", "}":"{" }
    stack = []
    for i in s:
        if i not in op.keys():
            stack.append(i)
        else:
            if op[i] != stack[-1]:
                print (False)
            else:
                stack.pop()
        print(stack)
    return True

isValid("([])")