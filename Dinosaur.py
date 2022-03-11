class Dinosaur:

    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def attack(self, robot):
        robot.health -= self.power





