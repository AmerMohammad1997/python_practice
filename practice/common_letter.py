def common_letter_str(str1: str, str2: str) -> dict:
    """common letters in 2 strings"""
    return set(str1.lower()) & set(str2.lower())


str1 = input(" enter string 1: ")
str2 = input("enter string 2: ")
print("common letters are "+ str(common_letter_str(str1, str2)))

def common_string(sts:dict, str1: dict) -> dict:
    return set(s.lower() for s in sts)& set(s.lower() for s in str1)

sts = {"amer", "mohd", "some"}
str1 = {"amer", "asdf", "some"}

print(common_string(sts, str1))