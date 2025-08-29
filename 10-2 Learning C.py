from pathlib import Path

path = Path("text_learning_python.txt")
content = path.read_text().rstrip()

lines = content.splitlines()
for line in lines:
    new_line = line.replace('Python', 'C++' )
    print(new_line)
