from business.Player import Player
from helpers import Room
from helpers.Menu import Menu
from helpers.Prompt import Prompt

rooms_matrix = [
    # A B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q
    [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],# A
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],# B
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],# C
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],# D
    [0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],# E
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],# F
    [0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],# G
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],# H
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],# I
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],# J
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],# K
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],# L
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],# M
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],# N
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],# O
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],# P
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0] # Q
]
print("Welcome to PythonSimpleGame !")
print()
print("You're in a castle and you have to escape from it.")
print("To do this you must brave the dangers on your way and find the exit.")
print()
player = Player(input("Please enter the name of your adventurer: "))
print("Good luck " + player.name)
print()
Menu.display_main_menu()
prompt_main_menu = Prompt.prompt("Choice: ", int, range(1, 6))
while prompt_main_menu != 5:
    if prompt_main_menu == 1:
        availables, possibilities = Menu.display_movement_menu(player.position, rooms_matrix)
        prompt_movement_menu = Prompt.prompt("Where do you want to go: ", int, range(1, possibilities + 1))
        player.move(availables, prompt_movement_menu)
        print()
        if player.position == 15:
            break
        else:
            Room.random(player)
            if player.health < 0:
                break
    elif prompt_main_menu == 2:
        player.display_inventory()
        input()
    elif prompt_main_menu == 3:
        player.display_player_statistics()
        input()
    else:
        player.show_map()
    Menu.display_main_menu()
    prompt_main_menu = Prompt.prompt("Choice: ", int, range(1, 6))
    print()
if prompt_main_menu == 5:
    print("You're a loser, you must never give up again.")
elif player.health > 0:
    print("Congratulations on getting out of the castle !!")
