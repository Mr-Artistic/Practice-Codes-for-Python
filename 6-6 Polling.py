fav_languages = {
    'Samad': 'C++',
    'Akash': 'Python',
    'Dhananjay': 'Java',
    'Ankita': 'Python',
    'Aishwarya': 'Python',
}

poll_list = ['Samad', 'Akash', 'Dhananjay', 'Ankita', 'Aishwarya', 'Rajesh', 'Ali', 'Rishika']

print("\nFor people who took the poll:\n")
for people in poll_list:
    if  people  in fav_languages.keys():
        print(f"Thank you {people} for your vote!")

print("\nFor people who have NOT took the poll:\n")
for people in poll_list:
    if people not in fav_languages.keys():
        print(f"{people}, please participate in the poll, ASAP!")

print("\nEnd of code. Exiting...")