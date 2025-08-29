from pathlib import Path

path = Path("text_learning_python.txt")
contents = path.read_text().rstrip().splitlines()

for content in contents:
    new_content = content.replace('Python', 'C++' )
    print(new_content)
