from business.Item import Item


class Equipment(Item):
    def __init__(self, name, size, power, type):
        super().__init__(name)
        self.size = size
        self.power = power
        self.type = type

    def display(self):
        print("Power: " + str(self.power))
        print("Type: " + str(self.type))
        print("Size: " + str(self.size))

