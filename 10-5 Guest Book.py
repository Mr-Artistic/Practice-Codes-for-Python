from pathlib import Path

session_active = True
guests = []

while session_active:
    guest = input("Enter your name (or 'q' to quit): ")
    if guest == '':
        print("Do not enter blanks")
    elif guest == 'q':
        session_active = False
        print("Ok. See you soon.")
    else:
        guests.append(guest)


path = Path("text_guest_book.txt")
path.write_text("\n".join(guests))
