character = input("Enter something: ")

if character.isalpha():
    print("It is an alphabet!")
elif character.isdigit():
    print("It is a number!")
else:
    print("It is a special symbol!")
