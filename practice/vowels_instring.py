def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count +=1
    return count

def count_consonent(text):
    vowels = "aeiouAEIOU"
    count ={}
    for s in text:
        if s not in vowels and s in count:
            count[s] = count[s] +1
        else:
            count[s] = 1
    return count

def count_consonants(text):
    result = {char: text.count(char) for char in text if char not in "aeiou"}
    return result

def extract_vowel (text: str) -> list:
    count ="aeiou"
    return list(set([char for char in text if char in count]))

text = "some text to check vowels"
print(f" {text} contains {count_vowels(text)} vowels")
print(f" Non vowel count {count_consonent(text)}")
print(extract_vowel(text))
print(count_consonants(text))