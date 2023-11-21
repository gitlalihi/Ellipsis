#Python function that takes an arbitrary number of arguments using *args and prints each argument. Use ... to represent unspecified arguments
var = ...

def print_arguments(*args):
    for i, arg in enumerate(args):
        print(f"Argument {i + 1}: {arg}")
    
    if not args:
        print(f"\nUnspecified arguments: {var}")

# Example usage:
print_arguments(1, 2, 3, "Python")
print_arguments()  