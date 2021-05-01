class Players:
    def __init__(self, name):
         self.gesture_list = {}
         self.name = name
         self.chosen_gesture = ""
         self.score = []

    def gesture_list(self):
        self.gesture_list = { 1:'Rock', 2:'Paper', 3:'Scissors', 4:'Lizard', 5:'Spock'}
        print(self.gesture_list.get([]))

    def name(self):
        self.name = input(" Create player: ")
        print(self.name)

    def chosen_gesture(self, chosen_gesture):
        self.chosen_gesture = chosen_gesture()
        if chosen_gesture is not self.gesture_list == True:
        elif self.gesture_list == chosen_gesture():
            print(chosen_gesture())

    def score(self, every_round_won, every_round):
        self.score ="+=1"
        print(self.score)
        every_round_won = every_round_won("earns you one point")
        while every_round_won in every_round:
            if every_round_won > 0 == every_round_won < 2:
                print(every_round_won)






