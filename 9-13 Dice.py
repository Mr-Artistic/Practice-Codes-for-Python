from random import randint

class Dice:
    def __init__(self, sides):
        """Initializes Dice Class."""
        self.side = sides

    def roll_die(self):
        """Prints a random number between 1 and number of side"""
        print(randint(1,self.side))


my_dice = Dice(100)
Dice.roll_die(my_dice)

