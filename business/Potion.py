from business.Item import Item


class Potion(Item):
    def __init__(self, name, power, effect):
        super().__init__(name)
        self.power = power
        self.effect = effect
