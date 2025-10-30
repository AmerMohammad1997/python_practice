given = "he is a python dev"
reversed_words = ' '.join(given.split(" ")[::-1])
print(reversed_words)


words =[]
word = ""
for each in given:
    if each !=" ":
        word += each
    else:
        words.append(word)
        word = ""
words.append(word)
print(words)

reversed_wor = " ".join(words[::-1])
print(reversed_wor)


# prints each 3rd number from list
lst = [1, 4, 2, 6, 4, 8, 90, 2, 45, 7, 8, 9]
result = lst[2::3]
print(result)



def reve_string(my_string):
    return my_string[::-1]

given_str = "hello"

reversed_string = "".join(reversed(given_str))
print(reversed_string)
print(reve_string(given_str))