given_val = "Enter sOME text tO mOdify in cases "
print("Lower case :", given_val.lower())
print("Upper case :", given_val.upper())
print("Title case :", given_val.title())
print("Capitalized : ", given_val.capitalize())
print("Swap case : ", given_val.swapcase())
manual_swapped = "".join([char.lower() if char.isupper() else char.upper() for char in given_val])
print("Manual swap ",manual_swapped)