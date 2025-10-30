import copy

#Original list

listi = [[1, 2], [2, 3], [3, 4]]

#Shallow copy
shallow_copy = copy.copy(listi)

# Deep copy
deep_copy = copy.deepcopy(listi)

#Modify the original list
listi[0][0] =99

print("After modifying list1:")

print("Original list1: ", listi)

print("Shallow copy:", shallow_copy)

print("Deep copy :", deep_copy)