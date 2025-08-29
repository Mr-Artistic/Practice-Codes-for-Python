current_users = ['samad', 'akash', 'dhananjay', 'ankita', 'admin']
new_users = ['Ankita', 'ADMIN', 'rajesh', 'aishwarya', 'rishika']

for user in new_users:
    if user.lower() in current_users:
        print(f"Dear '{user}', You need to change the UserName!")
    else:
        print(f"The UserName'{user}' is available!")