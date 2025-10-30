def is_palindrome (palindorme_input):
    revers_text = palindorme_input[::-1]
    return revers_text == palindorme_input

palindorme_input = input("enter string to check palindrome")
print(f" is the text palindrome or not : {is_palindrome(palindorme_input)}")