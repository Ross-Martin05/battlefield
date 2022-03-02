from weapons import Weapon

class Robot:

    def __init__(self, enter_name, enter_health) -> None:
        self.name = enter_name
        self.health = enter_health
        self.weapon = self.set_weapon()

    def set_weapon(self):
        list_of_weapons = [Weapon("Gun", 89), Weapon(
            "sword", 70), Weapon("taco_killer", 100)]
        return random.choice(list_of_weapons)