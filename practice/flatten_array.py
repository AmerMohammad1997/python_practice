# input =[1, [2, [3,4],5]]
#output =[1,2,3,4,5]

def insert_all_numver(input_val):
    list_all =[]
    for each in input_val:
        if isinstance(each, list):
            list_all.extend(insert_all_numver(each))
        else:
            list_all.append(each)
    return list_all


def using_recur_list(input_val):
    return [item for each in input_val for item in (using_recur_list(each) if isinstance(each, list) else [each])]

input_val =[1, [2, [3,4],5]]

print("Using normal loop", insert_all_numver(input_val))

print("Using list compre", using_recur_list(input_val))