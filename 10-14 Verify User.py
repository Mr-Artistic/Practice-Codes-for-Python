from pathlib import Path
import json

path = Path("json_username.json")

# Functions

def make_user_dict():
    """Makes User Dictionary when called and writes(overwrites) the data to json file."""
    name = input("Enter your username: ").lower()
    first = input("Enter your first name: ").lower()
    last = input("Enter your last name: ").lower()
    print("Thanks for registering!")

    user_dict = {'user_name': name, 'first_name': first, 'last_name': last}

    write_content = json.dumps(user_dict)
    path.write_text(write_content)

    return user_dict

def greet_user():
    """Greet the user."""
    print(f"Welcome {user_dict['user_name']}!")

def verify_user():
    """Verify the user."""
    verify_msg = input("\nPlease let us know if the username is correct (type 'yes/no'): ")
    if verify_msg.lower() == "yes":
        greet_user()

    elif verify_msg.lower() == "no":
        make_user_dict()

if path.exists():

    read_content = path.read_text()
    user_dict = json.loads(read_content)
    print(f" User Name: {user_dict['user_name']}")

    verify_user()

else:
    print("User file not found!")
    print()

    make_user_dict()




