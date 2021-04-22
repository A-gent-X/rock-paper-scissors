class Players:
    def __init__(self):
         self.gesture_list = ['Rock', 'Paper', 'Scissor', 'Lizard', 'Spock']
         self.name = ""
         self.chosen_gesture = ""
         self.chosen_gesture2 = ""
         self.chosen_gesture3 = ""
         self.score = ""

    def player_name(self):
        self.name = " name for player: "
        print(self.name)

    def chosen_gesture(self):
        self.chosen_gesture = "choose a gesture for", self.name
        print(self.chosen_gesture)

    def player_score(self):
        self.score = "every round won determines players score"
        print(self.score)






