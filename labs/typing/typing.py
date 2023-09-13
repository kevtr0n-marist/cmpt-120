# create a variable of type int
my_int = 1
my_float = 41.2
my_bool = False
my_str = "some text"

print(my_int)
print(my_float)
print(my_bool)
print(my_str)

print(type(my_str))
print(type(my_float))
print(type(my_bool))
print(type(my_str))

int_to_float = float(my_int)
float_to_int = int(my_float)
text = "123.456"
str_to_float = float(text)
float_to_str = str(my_float)

print(int_to_float)
print(float_to_int)
print(text)
print(str_to_float)
print(float_to_str)

error_var = float("Hello")
