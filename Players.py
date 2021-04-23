class Players:
    def __init__(self):
         self.gesture_list = ['Rock', 'Paper', 'Scissor', 'Lizard', 'Spock']
         self.name = ""
         self.chosen_gesture = ""
         self.score = ""

    def gesture_list(self):
        self.gesture_list = input['Rock', 'Paper', 'Scissor', 'Lizard', 'Spock']
        print(self.gesture_list)

    def player_name(self):
        self.name = input("name for player:")
        print(self.name)

    def chosen_gesture(self):
        self.chosen_gesture = input("choose a gesture for", self.name)
        print(self.chosen_gesture)

    def player_score(self):
        self.score = input("every round won contributes a point to players score")
        print(self.score)






