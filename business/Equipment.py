from business.Item import Item


class Equipment(Item):
    def __init__(self, name, size, power, type):
        super().__init__(name)
        self.size = size
        self.power = power
        self.type = type

