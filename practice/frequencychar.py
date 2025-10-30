def freq_of_words(stri: str) -> dict:
    """frequency of words in string"""
    count = {}
    words = stri.split(" ")
    for word in words:
        word = word.lower()
        if word not in count:
            count[word] = 0
        count[word] +=1
    return count

str1 = input("Enter a string to check word and its frequency: ")
print("frequency of words are: "+str(freq_of_words(str1)))

text = "aaaAAAA"
char_count = {char: text.count(char) for char in set(text)}
print(char_count)