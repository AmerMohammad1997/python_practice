def consonant_counter(given_str):
    vowels="aeiou "
    result = {const:given_str.lower().count(const) for const in set(given_str.lower()) if const not in vowels}
    return result

some_string = "thsi is thhhhhhe value"
print(consonant_counter(some_string))