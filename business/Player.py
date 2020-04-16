from tabulate import tabulate
from random import randrange
from helpers.Menu import Menu
from helpers.Prompt import Prompt


class Player:
    def __init__(self, name):
        self.max_health = 150.0
        self.health = self.max_health
        self.name = name
        self.equipment = []
        self.damages = 1
        self.armor = 0
        self.invetory_size = 30
        self.position = 0

    def display_inventory(self):
        table = []
        for e in self.equipment:
            table.append([e.name, e.type, e.power, e.size])
        print()
        print(str(self.equipments_size()) + "/" + str(self.invetory_size))
        print(tabulate(table, ["Name", "Type", "Power", "Size"]))

    def display_player_statistics(self):
        print(tabulate([
            ["Health", str(self.health) + "/" + str(self.max_health)],
            ["Damages", self.damages],
            ["Armor", self.armor],
            ["Inventory", str(self.equipments_size()) + "/" + str(self.invetory_size)]
        ]))

    def equipments_size(self):
        total = 0
        for e in self.equipment:
            total += e.size
        return total

    def heal(self, amount):
        self.health = round(self.health + amount, 1)
        if self.health > self.max_health:
            self.health = self.max_health
        print("You now have " + str(self.health) + "HP")

    def find_equipment(self, equipement):
        print("You find a " + equipement.name)
        equipement.display()
        while self.equipments_size() + equipement.size > self.invetory_size:
            print("You can't carry everything")
            Menu.display_too_heavy_menu()
            if Prompt.prompt("Choice: ", int, [1, 2]) == 1:
                equipement_amount = len(self.equipment) + 1
                Menu.display_throw_menu(self)
                prompt_throw_menu = Prompt.prompt("What do you want to drop ?  ", int, range(1, equipement_amount + 1))
                if prompt_throw_menu != equipement_amount + 1:
                    self.drop_equipment(prompt_throw_menu - 1)
                else:
                    print("You leave the " + equipement.name)
            else:
                print("You leave the " + equipement.name)
        self.take_equipment(equipement)

    def take_equipment(self, equipment):
        self.equipment.append(equipment)
        if equipment.type == "weapon":
            self.damages += equipment.power
        else:
            self.armor += equipment.power

    def drop_equipment(self, id):
        equipment = self.equipment[id]
        if equipment.type == "weapon":
            self.damages -= equipment.power
        else:
            self.armor -= equipment.power
        self.equipment.remove(equipment)

    def fight_monster(self, monster):
        monster.damages -= self.armor
        if monster.damages < 0:
            monster.damages = 0
        if randrange(0, 1) == 1:
            print("You attack first")
            input()
            monster.health -= self.damages
        else:
            print("The " + monster.name + " attacks first")
            input()
        while monster.health > 0 and self.health > 0:
            self.health -= monster.damages
            monster.health -= self.damages
        if self.health <= 0:
            print("You lost, try again")
        else:
            print("Well done, you beat the monster")
            self.health = round(self.health, 1)
            print("You have " + str(self.health) + "PV left")
