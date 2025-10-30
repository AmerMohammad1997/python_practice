text = "aaaAAAA"
char_count = {char: text.count(char) for char in set(text)}
print(char_count)
print()

powers = {x: x**3 for x in range(10)}
print(powers)
print()

original= {'amer':50, 'bob':40, 'chert': 90, 'das':15}
failed_persons = {k: v for k,v in original.items() if v <= 45}
results = {name: "pass" if marks> 45 else "fail" for name, marks in original.items()}
print("failed persons", failed_persons)
print()
print("check results", results.items())

for key, value in results.items():
    print(f"{key}: {value}")
print()

matrix = [[1, 2], [3, 4], [5, 6]]
flattened = [num for row in matrix for num in row]
print(flattened)




def sort_list(original_list):
    sorted_list=[]
    for each in original_list:
        if isinstance(each, list):
            sorted_list.extend(sort_list(each))
        else:
            sorted_list.append(each)
    return sorted_list

original_list= [1, [2, [3, [4,6]]]]
print(sort_list(original_list))

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
