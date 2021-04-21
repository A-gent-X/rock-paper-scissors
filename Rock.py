class Rock:

    def __init__(self):
        self.name = ""
        self.weakness = ""
        self.attack_type = ""

    def set_name(self):
        self.name = "Rock Lee"
        print(self.name)

    def set_weakness(self):
        self.weakness = "Sand Paper Shuriken"
        print(self.weakness)

    def set_attack_type(self):


        self.attack_type = "Boulder Barrage, Crush"
        print(self.attack_type)

class Metal(Rock):

    def __init__(self):
        self.attack_type = "Boulder Barrage, Crush"
        self.evovled_attack_type = "Meteoric Collision"
        super(). __init__()

    def __enchanced_physical_attribute(self):
        print(self.enchanced_durability)



    def set_name(self):
        self.name = ("Metal Lee")
        print(self.name)
