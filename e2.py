#Python function that takes a function as an argument and calls it with any number of arguments.
def call_function(func, *args, **kwargs):
    return func(*args, **kwargs)

def add(x, y):
    return x + y

result = call_function(add, x=10, y=22)
print(result)  

