from weapon import Weapon
import random

class Robot:

    def __init__(self, name, health) -> None:
        self.name = name
        self.health = health
        self.weapon = self.set_weapon()


    def set_weapon(self):
        list_of_weapons = [Weapon("Gun", 89), Weapon(
            "sword", 70), Weapon("taco_killer", 100)]
        return random.choice(list_of_weapons)


    def attack(self, dinosaur):
        dinosaur.health -= self.weapon.power