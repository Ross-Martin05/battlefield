from fleet import Fleet
from herd import Herd


class Battle:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()


    def run_game(self):
        self.display_welcome()
        self.battle()
        self.display_winners()

    def display_welcome(self):
        print("Welcome to Robots vs Dinosaurs!")

    def battle(self):
        while len(self.herd.dinosaur) > 0 and len(self.fleet.robot) > 0:
            dice_roll = random.randint(1, 10)
            if dice_roll % 2 == 0:
                self.dinosaur_turn()
            if len(self.fleet.robot) > 0:
                self.robot_turn()
            else:
                self.robot_()
            if len(self.herd.dinosaur) > 0:
                self.dinosaur_turn()

    def dinosaur_turn(self):
        self.show_dinosaur_opponent_options()
        dinosaur_choice = int(input("Which dinosaur will attack?"))
        print("")

        self.show_robot_opponent_options()
        robot_choice = int(input("Which robot will defend?"))
        print("")

        self.herd.dinosaur[dinosaur_choice].attack(self.fleet.robots[robot_choice])
        if self.fleet.robot[robot_choice].health <= 0:
            print(f"{self.fleet.robot[robot_choice].name} has died")
            self.fleet.robot.remove(sefl.robot[robot_choice])

    def robot_turn(self):
        self.show_robot_opponent_options()
        robot_choice = int(input("Which Robot will attack?"))
        print("")

        self.show_dinosaur_opponent_options()
        dinosaur_choice = int(input("Which dinosaur will defend?"))
        print("")

        self.fleet.robot[robot_choice].attack(self.herd.dinosaur[dinosaur_choice])
        if self.herd.dinosaur[dinosaur_choice].health <= 0:
            print(f"{slef.herd.dinosaur[dinosaur_choice].name} has died")
            self.herd.dinosaur.remove(slef.dinosaur[dinosaur_choice])

    def show_dinosaur_opponent_options(self):
        print("Choose your dinosaur")
        index = 0
        for dinosaur in self.herd.dinosaur:
            print(f"press {1, 2, 3} for {dinosaur.name} with {dinosaur.health} health")
            index += 1

    def show_robot_opponent_options(self):
        print("Choose your robot")
        index = 0
        for robot in self.fleet.robot:
            print(f"press {1, 2, 3} for {robot.name} with {robot.health} health")
            index += 1

    def display_winners(self):
        if len(self.fleet.robot) > len(slef.herd.dinosaur):
            print("Robots win!")
        else:
            print("Dinosaurs win!")