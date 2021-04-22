class Players:
    def __init__(self):
         self.gesture_list = ['Rock', 'Paper', 'Scissor', 'Lizard', 'Spock']
         self.name = ""
         self.chosen_gesture = ""
         self.score = ""

    def player_name(self):
        self.name = " name for player one: "
        print(self.name)

    def player_two(self):
        self.player_two_name = "David the Challenger"
        self.player_two_chooses = ['Spock', 'Rock', 'Scissors', 'Paper', 'Lizard']
        print(self.player_two_name)
        print(self.player_two_chooses)

