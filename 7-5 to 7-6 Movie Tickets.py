message = "\nPlease enter the ages for the participants."
message += "\nWrite quit once done: --> "

session_active = True
booking_made = False

while session_active:
    entry = input(message).lower()

    if entry == "quit":
        session_active = False
        break
    else:
        age = int(entry)
        booking_made = True
        if age < 3:
            print("This ticket is free!")
        elif age <= 12:
            print("This ticket is for $10.")
        elif age > 12:
            print("This ticket is $15.")

if booking_made == True:
    print("\nThanks for the bookings.")
else:
    print("Good Bye")