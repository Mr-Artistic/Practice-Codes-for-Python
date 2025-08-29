
message = "\nPlease enter the toppings you would like to have."
message += "\nEnter quit once done: "

entry = ""
while entry != "quit":
    entry = input(message).lower()
    if entry == "":
        print("Please don't enter blanks.")
    elif entry == "quit":
        break
    else:
        print(f"Sure, Adding {entry}!")

print("\nOk. Thanks for the order!")