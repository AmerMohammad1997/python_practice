def remove_char(given_string, index, new_text):
    # for each in given_string:
    if 0<= index <= len(given_string):
        return given_string[:index]+new_text+given_string[index:]
    else:
        return given_string + new_text

given_string = str(input("enter string: "))
index = int(input("enter index: "))
new_text = str(input("text to add: "))
print(f"new text {remove_char(given_string, index, new_text)}")