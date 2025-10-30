def sorted_brace(given_str) -> bool:
    stack = []
    cond_dict = {"}":"{","]":"[",")":"("}
    for each in given_str:
        if each in "{[(":
            stack.append(each)
        elif each in "}])":
            if not stack or stack[-1] != cond_dict[each]:
                return False
            stack.pop()
        return len(stack) == 0

given_str = "[{()]{{([])}}"
print(sorted_brace(given_str))