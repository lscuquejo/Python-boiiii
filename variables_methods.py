a = 5
b = 10
my_variable = 56
my_10_variable = 10


string_variable = "hello"
signle_quotes = 'strings can have single quotes'

#print(my_variable)
#print(string_variable)


def my_print_method(my_parameter):
    print(my_parameter)


def my_multiply_method(number_one, number_two):
    return number_one * number_two

result = my_multiply_method(5, 3)
#my_print_method(result)

my_print_method(my_multiply_method(5, 3))