from pygments.lexers import q

python_glossary = {
    'list' :        'Group of values stored in [].',
    'tuple' :       'Group of values stored in () and cannot be modified.',
    'set' :         'Group of "only values" stored in {}.',
    'dictionary' :  'Group of key and values (pairs) stored in {}.',
    'index' :       'The position of the values in a list/tuple.',
    'for' :         'The method used for doing something in a loop to all the values in the list/tuple.',
}

python_glossary['del'] = 'A statement to delete a value from the list.'
python_glossary['append'] = "A method used as .method()  to add a value to the end of a list."

print("\nEnter a python word you want to know to get its meaning.")
print(f"For example: If you enter 'List', you will get: '{python_glossary['list']}'")

word = input("\nEnter the word: ").lower()
print(f"{python_glossary.get(word, 'Sorry, No such word exist in the dictionary. Try another.')}")

print("\nHere  is the full glossary:\n")
for key, value in python_glossary.items():
    print(f"{key.title()}: {value}")

print("\nEnd of Code. Exiting...")