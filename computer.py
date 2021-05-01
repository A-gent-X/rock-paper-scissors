from players import Players

class Computer(Players):
    def __init__(self):
        self.AI = ""
        self.advanced_AI = ""
        super(). __init__()

    def set_AI(self):
        self.AI = "Beta"
        print(self.AI)

    def set_advance_AI(self):
        self.advanced_AI = "Alpha T90"
        print(self.advanced_AI)
