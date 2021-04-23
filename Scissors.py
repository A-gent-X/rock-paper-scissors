class Scissors:
    def __init__(self):
        self.name = ""
        self.weakness = ""
        self.attack_type = ""

    def set_name(self):
        self.name = "Slasher"
        print(self.name)

    def set_weakness(self):
        self.weakness = "Boulder Barrage"
        print(self.weakness)

    def set_attack_type(self):

class Blade(Scissors):

    def __init__(self):
        self.attack_type = "Lethal Incision, Slash"
        self.evovled_attack_type = "Invisible Slash, Slash"
        super().__init__()

    def __enchanced_physical_attribute(self):
        self.enchanced_physical_attribute = "enchanced precision"
        self.enchanced_physical_attribute = "increase attack strength"
        print(self.enchanced_precision)

    def set_name(self):
        self.name = ("Metal Lee")
        print(self.name)
        \


