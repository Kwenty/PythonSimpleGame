import math
from random import randrange

from business.Equipment import Equipment
from business.Monster import Monster

places = [
    "Armoury",
    "Torture room",
    "Jail",
    "Trophy room",
    "Kitchen"
]
monsters = [
    "Spider",
    "Zombie",
    "Ghost"
]
weapons = [
    "Sword",
    "Axe",
    "Bow",
    "Spear",
    "Club"
]

armors = [
    "Helmet",
    "Shield",
    "Breastplate",
    "Boots",
    "Leggings",
    "Armbands"
]


def random(player):
    print("You are arriving in " + places[randrange(0, len(places))])
    event = randrange(6)
    if event == 0:  # weapon
        weapon = random_equipment(player.position + 1, "weapon", weapons[randrange(0, len(weapons))])
        player.find_equipment(weapon)
    elif event == 1:  # armor
        armor = random_equipment(player.position + 1, "armor", armors[randrange(0, len(armors))])
        player.find_equipment(armor)
    elif event == 2:  # potion
        potion_power = round((player.position + 1) * randrange(10, 20) / 8, 1)
        print("You find a potion and retrieve " + str(potion_power) + " HP")
        player.heal(potion_power)
    elif event == 3:  # nothing
        print("Nothing special happens")
    else:  # ennemy
        monster = random_monster(player.position + 1)
        monster.display()
        print()
        player.fight_monster(monster)
    input()


def random_monster(position):
    return Monster(
        monsters[randrange(0, len(monsters))],
        position * randrange(10, 17),
        position * randrange(10, 17) / 10
    )


def random_equipment(position, equipment_type, name):
    return Equipment(
        name,
        round(math.sqrt(position * randrange(20, 40) / 10), 1),
        position * randrange(10, 20) / 10,
        equipment_type
    )
