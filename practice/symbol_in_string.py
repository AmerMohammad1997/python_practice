def add_sym_even(given_str):
    result = ""
    for letter in range(len(given_str)):
        if (letter+1)% 2 ==0:
            result += "#"
        else:
            result +=given_str[letter]
    return result

given_str = "the quick brown fox"
print(add_sym_even(given_str))

# using comprehension
result ="".join([given_str[i] if (i+1) % 2 != 0 else "$" for i in range(len(given_str)) ])

print(result)