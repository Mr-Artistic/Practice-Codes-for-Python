class Restaurant:
    def __init__(self, name, cuisine):
        """Initializes name and cuisine."""
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        """Prints restaurant name and cuisine."""
        print(f"{self.name} has {self.cuisine} cuisine.")

    def open_restaurant(self):
        """Prints that restaurant is open."""
        print(f"And {self.name} is now open!")

    def set_number_served(self, number_served):
        """Sets restaurant number served."""
        self.number_served = number_served

    def increment_number_served(self, number_served):
        """Increments restaurant number served."""
        self.number_served += number_served

my_restaurant = Restaurant("Neo Woods", "North-Indian")
your_restaurant = Restaurant("Thanda Mamla", "South-Indian")
their_restaurant = Restaurant("Govind Garden", "International")

my_restaurant.set_number_served(23)
my_restaurant.increment_number_served(10)

print(f"Restaurant Name: {my_restaurant.name}")
print(f"Cuisine: {my_restaurant.cuisine}")
print(f"Customers Served: {my_restaurant.number_served}")
