class Battle:


    def Battle(self, enemy):
        if enemy.health > self.attack:
            enemy.health = enemy.health - self.attack
        else:
            enemy.health = 0