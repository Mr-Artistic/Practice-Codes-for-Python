from pathlib import Path

file_names = ['text_cats.txt', 'text_dogs.txt']

for file_name in file_names:
    path = Path(file_name)

    try:
        content = path.read_text()
        print(content)
        print()

    except FileNotFoundError:
        print(f"File not found in {path}.")
        # replace the above line with 'pass' for 10-9.


