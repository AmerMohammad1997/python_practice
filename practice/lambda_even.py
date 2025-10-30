def even_number(numb):
    even_numbers = list(filter(lambda x: x % 2 == 0, numb))
    return even_numbers

numbe = input("enter list of numbers separated by comma: ")
numbe = [int(x) for x in numbe.split(',')]
print(f"even numbers in the list are: {even_number(numbe)}")