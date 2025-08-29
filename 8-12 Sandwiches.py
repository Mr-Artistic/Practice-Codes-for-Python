def my_sandwich(*user_input):
    """Prints the list of items user wants in the sandwich."""
    for item in user_input:
        print(f"Your sandwich with {item} is being prepared.")

my_sandwich('cheese', 'pepper', 'money')
