
# create a function
def hello():
    print("Hello world!")

# create a function named add_numbers that takes two arguments and returns the sum.
def add_numbers(a, b):
    return a + b

def to_list(*args):
    result = []
    for i in args:
        result.append(i)
    return result

hello()
print(add_numbers(5, 6))
print(to_list(1, 2, 5, {}, [], "", 0x00))