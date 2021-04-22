from Players import Players

class Human(Players):
    def __init__(self):
        self.intuition = ""
        self.good_fortune = ""
        super(). __init__()

    def set_intuition(self):
        self.intuition = "ability to learn and predict patterns quickly"
        print(self.intuition)

    def set_strategist(self):
        self.good_fortune = "luck of the draw"
        print(self.good_fortune)