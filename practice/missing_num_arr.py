def missing_num(all_num):
    min_num = min(all_num)
    max_num = max(all_num)
    missing = set(range(min_num, max_num))
    missing_n = missing-set(all_num)
    return missing_n

all_num = {4,7,7,0,4,1}
common = {2,5,4,6,7,8,1}
print(missing_num(all_num))
min = min(common)
max = max(common)
unique_vals = set(all_num)

result = {i for i in range(min, max+1) if i in common & all_num}
print(result)