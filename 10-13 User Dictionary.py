from pathlib import Path
import json

path = Path("json_username.json")

if path.exists():
    read_content = json.loads(path.read_text())
    for key, value in read_content.items():
        print(f"{key}: {value.title()}")

else:
    name = input("Enter your username: ").lower()
    first = input("Enter your first name: ").lower()
    last = input("Enter your last name: ").lower()

    user_dict = {'user_name': name, 'first_name': first, 'last_name': last}

    write_content = json.dumps(user_dict)
    path.write_text(write_content)

