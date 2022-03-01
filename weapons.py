class Weapon:

    def __init__(self, weapon_name, attack_power):
        self.weapon = weapon_name
        self.power = attack_power

    

gun = Weapon("Gun", 89)

sword = Weapon("Sword", 70)

killer_taco = Weapon("Killer taco", 100)

weapons_list = [gun, sword, killer_taco]



