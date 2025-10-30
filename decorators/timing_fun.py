import time

def timer(func):

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        endtime = time.time()
        result_set = (f"{endtime-start} {result}")
        print(result_set)
        return result_set
    return wrapper

@timer
def say_hello():
    print("say hello called")
    time.sleep(4)
    print("after sleep")
    return "result from say helo"

say_hello()