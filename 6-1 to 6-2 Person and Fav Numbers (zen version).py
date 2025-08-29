# THIS IS THE ZEN VERSION.
# You will get to learn this in detail soon in this chapter.

# A User input is added with two level authentication.
# A loop is used to print fav nums.

# Let's first import 'Date' from DateTime module to insert date value in the dictionary.
from datetime import date

# Dictionary starts here.
friends = [
    {
        'first_name': 'Samad',
        'last_name': 'Mughal',
        'dob': date(1992,5, 1),
        'gender': 'Male',
        'city' : 'Lonavala',
        'fav_number' : 2,
    },

    {
        'first_name': 'Akash',
        'last_name': 'Tikande',
        'dob': date(1997,8, 14),
        'gender': 'Male',
        'city' : 'Bhosari',
        'fav_number' : 5,
    },

    {
    'first_name': 'Dhananjay',
    'last_name': 'Sriwastwa',
    'dob': date(1988,10, 27),
    'gender': 'Male',
    'city' : 'Delhi',
    'fav_number' : 7,
    },

    {
    'first_name': 'Ankita',
    'last_name': 'Chavan',
    'dob': date(2001,1, 5),
    'gender': 'Female',
    'city' : 'Satara',
    'fav_number' : 1,
    },

    {
    'first_name': 'Aishwarya',
    'last_name': 'Renukar',
    'dob': date(1996,8, 11),
    'gender': 'Female',
    'city' : 'Pune',
    'fav_number' : 9,
    },

]

# Action starts here.
admin_pwd = input("\nEnter Admin Password: ")

if admin_pwd == "12345":

    name = input("Whose Biodata do you want? :  ")
    for friend in friends:
        if friend['first_name'] == name.title():
            print(f"\nThe biodata of {friend['first_name']} is:\n")
            print(f"First Name: {friend['first_name']}")
            print(f"Last Name: {friend['last_name']}")
            print(f"Birth Date (YYYY-MM-DD): {friend['dob']}")
            print(f"Gender: {friend['gender']}")
            print(f"City: {friend['city']}")

            ask = input("\nDo you want to get fav numbers of ALL the friends? Enter (yes/no):  ")
            if ask.lower() == 'yes':
                pwd = input("Enter password: ")
                if pwd == '54321':
                    print('')
                    for friend in friends:
                        print(f"{friend['first_name']}'s favourite number is {friend['fav_number']}.")
                    print("\nEnd of Code. Exiting...")
                else:
                    print("Wrong Password! Exiting...\n")
            elif ask.lower() == 'no':
                print("Ok Bye.\n\nExiting...\n")
            else:
                print("Please type 'yes' or 'no' only (Re-run the code).")
                print("\nEnd of code. Exiting...")

            break

    else:
        print("No such friend exists! \n\nExiting...\n")

else:
    print("Wrong Password! Exiting...\n")