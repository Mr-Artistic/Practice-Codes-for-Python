
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

class IceCreamStand(Restaurant):

    def __init__(self, name, cuisine, flavour):
        """Initializes attributes of Restaurant."""
        super().__init__(name, cuisine)
        self.flavour = flavour

    def display_flavoured(self):
        """Prints flavour of ice cream."""
        print(f"The ice cream is {self.flavour} flavoured.")


my_restaurant = Restaurant("Neo Woods", "North-Indian")
my_ice_cream_stand = IceCreamStand("Neo Woods Ice Cream Stall", "North-Indian", flavour="chocolate")
your_restaurant = Restaurant("Thanda Mamla", "South-Indian")
their_restaurant = Restaurant("Govind Garden", "International")

print(f"My Ice Cream Stall Name is: {my_ice_cream_stand.name}.")
print(f"The ice cream's flavour is: {my_ice_cream_stand.flavour}.")

