from players import Players

class Human(Players):
    def __init__(self):
        self.challenger = ""
        self.challengerOne = ""
        super(). __init__()

    def set_challenger(self):
        self.challenger = "Professor X"
        print(self.challenger)

    def set_challengerOne(self):
        self.challengerOne = "Satish the Skater"
        print(self.challengerOne)




