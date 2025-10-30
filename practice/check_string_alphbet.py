def alphabetically_sorted(tex):
    return list(tex) == sorted(tex)

string_val = "parrst"

if alphabetically_sorted(string_val):
    print("True")
else:
    print("False")

result = "".join([f"True" if list(string_val) == sorted(string_val) else "False" ])
print(result)