class Monster:
    def __init__(self, name, health, damages):
        self.name = name
        self.health = health
        self.damages = damages

    def display(self):
        print("A " + self.name + " appears")
        print("Health: " + str(self.health))
        print("Damages: " + str(self.damages))
