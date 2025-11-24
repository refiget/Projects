class Hero():
    def __init__(self, name, hp, attack ):
        self.name = name
        self.hp = hp
        self.attack = attack


    def attack_enemy(self, enemy):
        print(f"{self.name } have attacked the Monster.")
        enemy.take_damage(self.attack)

class Monster():
    def __init__(self, hp):
        self.hp = hp

    def take_damage(self, amount):
        self.hp -= amount
        print(f"Monster takes {amount} damage")

        if self.hp <= 0:
            print("Monster is dead!")


bob = Hero("MathMaster", 100, 10)
monster = Monster(20)

bob.attack_enemy(monster)
bob.attack_enemy(monster)
        

        



