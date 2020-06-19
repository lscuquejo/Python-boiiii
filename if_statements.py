know_people = ["John", "Anna", "Mary"]
person = input("Enter the person you know: ")

if person in know_people:
    print("You know {}".format(person))
else:
    print("You don't know {}!".format(person))