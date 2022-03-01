from Dinosaur import Dinosaur

import random

dino_1 = Dinosaur("mothra", 100, 75)

dino_2 = Dinosaur("Godzilla", 100, 90)

dino_3 = Dinosaur("Dino Taco", 100, 99)

dino_list = {dino_1, dino_2, dino_3}

def get_random_dino(list):
    return random.choice(list)

random_dino = get_random_dino(dino_list)

print(random_dino)