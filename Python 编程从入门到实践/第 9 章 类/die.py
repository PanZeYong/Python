from random import randint

class Die():
    """随机数"""
    x = randint(1, 6);

    def __init__(self):
        self.sides = 6;

    def roll_die(self):
        print("X: " + str(self.x))

die = Die()
die.roll_die()