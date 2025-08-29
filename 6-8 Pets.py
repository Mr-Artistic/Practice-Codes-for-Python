pets = {

    'cat': {
        'species': 'Cat',
        'name': 'Feli',
        'age': 1,
        'owner': 'Samad',
    },


    'horse' : {
        'species': 'Horse',
        'name': 'Fellow',
        'age': 7,
        'owner': 'Akash',
    },

    'dog' : {
        'species': 'Dog',
        'name': 'Fellah',
        'age': 3,
        'owner': 'Dhananjay',
        },
}

for pet, info in pets.items():
    print(f"Pet: {pet.title()}")
    print(f"Name: {info['name']}")
    print(f"Age: {info['age']}")
    print(f"Owner: {info['owner']}\n")
