friends = ['Samad', 'Akash', 'Dhananjay', 'Ankita', 'Aishwarya', 'Rishika']

print("My oldest friends are:\n")
for friend in friends[:3]:
    print(friend)

print("\nMy best friends are:\n")
for friend in friends[1:4]:
    print(friend)

print("\nMy new friends are:\n")
for friend in friends[-3:]:
    print(friend)

