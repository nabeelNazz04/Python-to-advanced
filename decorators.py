# Decorators in Python (Brief Overview)

## Definition:
'''
A decorator in Python is a design pattern that allows you to modify or enhance the behavior of a function or method without permanently changing its structure. They are implemented as callable objects (functions or classes) that wrap another function or method.
'''


### Key Concepts:
'''
1. **Higher-Order Functions:**
   - A function that accepts another function as an argument or returns a function.
   - Decorators are built on the concept of higher-order functions.

2. **Function Wrapping:**
   - A decorator takes a function, adds some functionality, and returns the modified function.

3. **Syntax Sugar:**
   - Decorators are applied using the `@decorator_name` syntax placed above the function definition.
'''


### Anatomy of a Decorator:
'''
def decorator(func):
    def wrapper(*args, **kwargs):
        # Code to execute before the original function
        print("Before function call")
        result = func(*args, **kwargs)
        # Code to execute after the original function
        print("After function call")
        return result
    return wrapper
'''

## Example: Using a Decorator to Measure Execution Time

### Without Decorators:

import time

def calc_square(numbers):
    start = time.time()
    result = []
    for number in numbers:
        result.append(number * number)
    end = time.time()
    print("calc_square took " + str((end - start) * 1000) + ' milliseconds')
    return result

def calc_cube(numbers):
    start = time.time()
    result = []
    for number in numbers:
        result.append(number * number * number)
    end = time.time()
    print("calc_cube took " + str((end - start) * 1000) + ' milliseconds')
    return result

if __name__ == "__main__":
    numbers = range(1, 10000)
    calc_square(numbers)
    calc_cube(numbers)

### With Decorators:

import time

def time_it(func):
    """Decorator to measure the execution time of a function."""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {str((end - start) * 1000)} milliseconds")
        return result
    return wrapper

@time_it
def calc_square(numbers):
    result = []
    for number in numbers:
        result.append(number * number)
    return result

@time_it
def calc_cube(numbers):
    result = []
    for number in numbers:
        result.append(number * number * number)
    return result

if __name__ == "__main__":
    numbers = range(1, 10000)
    calc_square(numbers)
    calc_cube(numbers)


### Explanation:
'''
1. **Without Decorators:**
   - The time measurement logic is repeated in each function.
   - This makes the code less readable and harder to maintain.

2. **With Decorators:**
   - The `time_it` decorator abstracts the time measurement logic.
   - The `@time_it` syntax is applied above the functions to enhance their behavior.
   - This keeps the function logic clean and reusable.

'''



### Output:
'''
calc_square took X milliseconds
calc_cube took Y milliseconds
'''

