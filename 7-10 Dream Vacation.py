message = "\nIf you could visit one place in the world, where would you go? "
message += "\nEnter quit once done (you can poll multiple places): "

places = {}

poll_active = True
poll_done = False

while poll_active:

    place = input(message).lower()
    if place == "":
        print("Please don't enter blanks!")
    elif place == 'quit':
        poll_active = False
        break

    else:
        name = input("Enter your name: ").lower()
        poll_done = True
        poll_active = True
        if name not in places:
            places[name] = []

        places[name].append(place)


if poll_done == True:
    print("\nThanks for the poll.")
    print("\n----- THE POLL RESULTS ARE -----\n")

    for name, place in places.items():
        print(f"{name} wants to visit {place}.")

else:
    print("\nOk. Bye.\n")
