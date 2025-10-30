def my_decorator(omg):
    def hello_wrapper():
        print("started hello wrapper")
        result =omg()
        print("say hello completed")
        print("result for sayhello", result)
    return hello_wrapper

@my_decorator
def say_hello():
    return "Say hello returned response"

say_hello()

def logger(func):

    def wrapper(original_list):
        result = func(original_list)
        return result
    return wrapper

@logger
def sort_list(original_list):
    sorted_list = []
    for each in original_list:
        if isinstance(each, list):
            sorted_list.extend(sort_list(each))
        else:
            sorted_list.append(each)
    return sorted_list

# Example usage
nested= [1, [2, [3, 4]], 5]
print(sort_list(nested))