my_variable = "hello"

list_grades = [99, 80, 90]
tuple_grades = (77, 80, 90, 100, 105) # immutable
set_grades = {77, 80, 90, 100} # unique & unnordered

list_grades.append(100) # add a value to a list
#print(list_grades)

# Set operations

your_lottery_numbers = {1, 2, 3, 4, 5}
winning_numbers = {1, 3, 5, 7, 9, 11}

#print(your_lottery_numbers.intersection(winning_numbers))

print(your_lottery_numbers.union(winning_numbers))