from pathlib import Path
import json

path = Path('json_favourite_number.json')

if path.exists():
    user_content = json.loads(path.read_text())
    print(f"Your fav numbers are already saved with us: {user_content}")
    print(f"Hence, exiting...")

else:

    session_active = True
    fav_numbers = []

    while session_active:
        fav_num = input("Enter a favorite number (or 'q' to quit): ")

        if fav_num:

            if fav_num == 'q':
                session_active = False
            else:
                try:
                    number = int(fav_num)
                    fav_numbers.append(number)
                    content = json.dumps(fav_numbers)
                    path.write_text(content)
                except ValueError:
                    print("Enter numbers only and not strings.\n")

        else:
            print("Do not enter blanks.\n")
