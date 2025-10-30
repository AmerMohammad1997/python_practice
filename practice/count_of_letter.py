def count_char(stri:str):
    count ={}
    str1 = stri.replace("","")
    for ch in stri.lower():
        if ch in count:
            count[ch] = count[ch] +1
        else:
            count[ch] = 1
    return count

str1 = input("Please enter a string to check count: ").replace(" ","").lower()
print(str(count_char(str1)))


char_count = { char : str1.count(char) for char in set(str1)}
print(char_count)





even_numbers = [num for num in range(0,10) if num %2==0]
print(even_numbers)

string = "Hi i am developer"
non_vowels="".join([ch for ch in string if ch.lower() not in "aeiou"])
print(non_vowels)