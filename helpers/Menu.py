from tabulate import tabulate


class Menu:
    @staticmethod
    def display_main_menu():
        print("1. Change room")
        print("2. Inventory")
        print("3. Player statistics")
        print("4. Give up")

    @staticmethod
    def display_movement_menu(position, rooms_matrix):
        availables = []
        for index, room in enumerate(rooms_matrix[position]):
            if room == 1:
                availables.append(index)
        i = 0
        data = {}
        for p in availables:
            i += 1
            print(str(i) + ". Go to room " + str(chr(p + 65)))
            data[i] = p
        return [data, i]

    @staticmethod
    def display_too_heavy_menu():
        print("1. Throw something")
        print("2. Leave the equipment")

    @staticmethod
    def display_throw_menu(player):
        table = []
        for index, e in enumerate(player.equipment):
            table.append([index + 1, e.name, e.type, e.power, e.size])
        table.append([index + 2, "Forgive"])
        print(tabulate(table, ["ID", "Name", "Type", "Power", "Size"]))
