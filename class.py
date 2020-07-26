'''

This is the program for creating classes assignment.

'''

# Import libraries
import random


class Monster():
    
    # Construct the class variables
    def __init__(self, name, level, hp, damage):
        self.name = name
        self.level = level
        self.hp = hp
        self.damage = damage
    

    # Attack method
    def attack(self, target):
        target.hp = target.hp - self.damage
        return target.hp
    

    # Drop exp and items
    def drop(self):
        random.seed(0)
        drop_exp = random.randint(0.9 * self.level, 1.1 * self.level)

        return drop_exp
    

class Player(Monster):

    # Use items to increase damage
    def use(self, hp, item):
        return hp - item.damage - self.damage


class Item():

    # Construct the class variables
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage


def main():
    # Create player
    player = Player('Skywalker', 99, 9999, 999)

    # Create monster
    monster = Monster('Darth Vader', 99, 12000, 1200)

    while player.hp >= 0 or monster.hp >= 0:
        monster_hp = monster.hp
        player_hp = player.hp
    
        player.attack(monster)
        print('You deals {damage} damage to {target}. The monster has {hp} HP left.'.format(damage = monster.hp - monster_hp, target = monster.name, hp=monster.hp))

        monster.attack(player)
        print('Monster deals {damage} damage to you. You have {hp} HP left.'.format(damage = player.hp - player_hp, hp = player.hp))

        if player.hp <= 0:
            print('You are killed by {monster}.'.format(monster = monster.name))
            break

    return None

main()