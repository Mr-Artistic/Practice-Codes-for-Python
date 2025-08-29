from pathlib import Path

path = Path("text_learning_python.txt")
content = path.read_text().rstrip()

print(content)
print()

lines = path.read_text().splitlines()
for line in lines:
    print(line)
