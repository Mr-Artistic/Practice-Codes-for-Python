guests = ['Samad', 'Akash', 'Dhananjay', 'Ankita', 'Aishwarya']

print(f"Guest List: {guests}")

print(f"\nHi {guests[0]}, Would you like to have dinner with me?")
print(f"Hi {guests[1]}, Would you like to have dinner with me?")
print(f"Hi {guests[2]}, Would you like to have dinner with me?")
print(f"Hi {guests[3]}, Would you like to have dinner with me?")
print(f"Hi {guests[4]}, Would you like to have dinner with me?")

print(f"\nAs {guests[3]} is no longer my friend, she cannot make it.")
guests.remove('Ankita')
print(f"\nUpdated List: {guests}")

print(f"\nAs I have made 3 new friends, I am adding them in the list.")
guests.insert(0, 'Rajesh')
guests.insert(3, 'Ali')
guests.append('Rishika')

print(f"\nUpdated List: {guests}")

print(f"\nHi {guests[0]}, Would you like to have dinner with me?")
print(f"Hi {guests[1]}, Would you like to have dinner with me?")
print(f"Hi {guests[2]}, Would you like to have dinner with me?")
print(f"Hi {guests[3]}, Would you like to have dinner with me?")
print(f"Hi {guests[4]}, Would you like to have dinner with me?")
print(f"Hi {guests[5]}, Would you like to have dinner with me?")
print(f"Hi {guests[6]}, Would you like to have dinner with me?")

print("\nUnfortunately, at the last moment I get to know that only 2 seats are available in the hotel. Hence, I am bound to invite only two of you.")

dg0 = guests.pop(0)
print(f"\nSorry {dg0}, we will dine another day.")

dg1 = guests.pop(0)
print(f"Sorry {dg1}, we will dine another day.")

dg2 = guests.pop(0)
print(f"Sorry {dg2}, we will dine another day.")

dg3 = guests.pop(0)
print(f"Sorry {dg3}, we will dine another day.")

dg4 = guests.pop(0)
print(f"Sorry {dg4}, we will dine another day.")

print(f"\nHi {guests}, do not worry. You are going to come with me today.")

del guests[0]
del guests[0]
print(f"\nAfter dinner:{guests}")