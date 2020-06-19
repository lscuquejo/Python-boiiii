my_string = "hello"

for character in my_string:
    print(character)

my_list = [1, 3, 5, 7, 9]

for number in my_list:
    print(number ** 2)

user_wants_number = True
while user_wants_number == True:

    user_input = input("Should we print the number 10? (y/n)")
    if user_input == 'n':
        user_wants_number = False
    elif user_input == 'y':
        print(10)
        user_input = True
    else:
        print("Please write y or n")