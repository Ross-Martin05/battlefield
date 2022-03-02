class Weapon:

    def __init__(self, weapon_name, attack_power) -> None:
        self.weapon = weapon_name
        self.power = attack_power

    
    def __str__(self) -> str:
        return f"{self.name}: Attack Power - {self.attack_power}"

        
gun = Weapon("Gun", 89)

sword = Weapon("Sword", 70)

killer_taco = Weapon("Killer taco", 100)





