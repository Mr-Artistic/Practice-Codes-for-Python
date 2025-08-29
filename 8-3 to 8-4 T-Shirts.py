def make_shirt(quote, size='large'):
    """Tells about the size and quote of the shirt."""
    print(f"\nYour T-Shirt's size is: {size.title()}, and the quote is: '{quote}'")

make_shirt("I love Python!")
make_shirt("I love Python!", size='medium')
make_shirt("I love MySQL!", size='small')
