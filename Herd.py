from dinosaur import Dinosaur

class Herd:

    def __init__(self) -> None:
        self.dinosaur = Dinosaur(name, health, power)
        self.dino_list = []

    def create_herd(self):   
        dino_1 = Dinosaur("mothra", 100, 75)
        dino_2 = Dinosaur("Godzilla", 100, 90)
        dino_3 = Dinosaur("Dino Taco", 100, 99)
        self.dino_list.extend([dino_1, dino_2, dino_3])
