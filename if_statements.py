#know_people = ["John", "Anna", "Mary"]
#person = input("Enter the person you know: ")

#if person in know_people:
#    print("You know {}".format(person))
#else:
#    print("You don't know {}!".format(person))

def who_do_you_know():
    people_user_knows = input("Enter a list of people you know:")
    return people_user_knows.split()

def ask_user(people_user_knows_param):
    person = input("Enter the name of a know person :)")

    if person in people_user_knows_param:
        print("You know {} !!!".format(person))
    else:
        print("You don't know {} !!!".format(person))

users_answer = who_do_you_know()

ask_user(users_answer)
