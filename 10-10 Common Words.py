from pathlib import Path

path = Path("text_pride_and_prejudice.txt")
text = path.read_text(encoding='utf-8').lower()
the_count = text.count('the ')

# Some additional analysis (analysing the frequency of word: 'the') -->

words = text.split()
word_count = len(words)

the_ratio = round(the_count / word_count * 100, 2)

print(f"Word Count: {word_count}, 'The' Count: {the_count}.")
print(f"'The' Ratio is {the_ratio}%")