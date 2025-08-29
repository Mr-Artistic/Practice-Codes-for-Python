# Let's first import 'Date' from DateTime module to insert date value in the dictionary.
from datetime import date

bio_samad = {
    'first_name': 'Samad',
    'last_name': 'Mughal',
    'dob': date(1992,5, 1),
    'gender': 'Male',
    'city' : 'Lonavala',
    'fav_number' : 2,
    }

print("The biodata of Samad is:\n")
print(f"First Name: {bio_samad['first_name']}")
print(f"Last Name: {bio_samad['last_name']}")
print(f"Birth Date (YYYY-MM-DD): {bio_samad['dob']}")
print(f"Gender: {bio_samad['gender']}")
print(f"City: {bio_samad['city']}")

bio_akash = {
    'first_name': 'Akash',
    'last_name': 'Tikande',
    'dob': date(1997,8, 14),
    'gender': 'Male',
    'city' : 'Bhosari',
    'fav_number' : 5,
    }

bio_dhananjay = {
    'first_name': 'Dhananjay',
    'last_name': 'Sriwastwa',
    'dob': date(1988,10, 27),
    'gender': 'Male',
    'city' : 'Delhi',
    'fav_number' : 7,
    }

bio_ankita = {
    'first_name': 'Ankita',
    'last_name': 'Chavan',
    'dob': date(2001,1, 5),
    'gender': 'Female',
    'city' : 'Satara',
    'fav_number' : 1,
    }

bio_aishwarya = {
    'first_name': 'Aishwarya',
    'last_name': 'Renukar',
    'dob': date(1996,8, 11),
    'gender': 'Female',
    'city' : 'Pune',
    'fav_number' : 9,
    }

print(f"\n{bio_samad['first_name']}'s favourite number is {bio_samad['fav_number']}.")
print(f"{bio_akash['first_name']}'s favourite number is {bio_akash['fav_number']}.")
print(f"{bio_dhananjay['first_name']}'s favourite number is {bio_dhananjay['fav_number']}.")
print(f"{bio_ankita['first_name']}'s favourite number is {bio_ankita['fav_number']}.")
print(f"{bio_aishwarya['first_name']}'s favourite number is {bio_aishwarya['fav_number']}.")
