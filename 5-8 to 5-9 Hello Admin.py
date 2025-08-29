usernames = ['samad', 'akash', 'dhananjay', 'ankita', 'admin']
if usernames == [] :
    print('We need some users!')
else:
    input_user = input("Enter UserName: ")

    if input_user in usernames:
        if input_user == 'admin':
            print(f"Hello {input_user.upper()}, would you like to access the dashboard?")
        else:
            print(f"Hello {input_user.title()}, Welcome back!")
    else:
        print(f"Sorry, the user '{input_user}' doesn't exist.")
