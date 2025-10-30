given_string = "some text to check"
str_tocheck = "my"

if str_tocheck in given_string:
    print(f" {str_tocheck } is present ")
else:
    print(f" {str_tocheck } is not present ")

check = [f"{str_tocheck} is present" if str_tocheck in given_string else f"{str_tocheck} is not present"  ]
print(check)

