class Restaurant:
    def __init__(self, name, cuisine):
        """Initializes name and cuisine."""
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        """Prints restaurant name and cuisine."""
        print(f"{self.name} has {self.cuisine} cuisine.")

    def open_restaurant(self):
        """Prints that restaurant is open."""
        print(f"And {self.name} is now open!")

my_restaurant = Restaurant("Neo Woods", "North-Indian")
your_restaurant = Restaurant("Thanda Mamla", "South-Indian")
their_restaurant = Restaurant("Govind Garden", "International")

print(my_restaurant.name)
print(my_restaurant.cuisine)

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

my_restaurant.describe_restaurant()
your_restaurant.describe_restaurant()
their_restaurant.describe_restaurant()