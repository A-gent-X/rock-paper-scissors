class Players:
    def __init__(self):
        self.player_one_name = ""
        self.player_two_name = ""
        self.player_one_chooses = ""
        self.player_two_chooses = ""


    def player_one(self):
        self.player_one_name = "Goliath the Conquer"
        self.player_one_chooses = ['Rock', 'Paper', 'Spock', 'Lizard', 'Scissors']
        print(self.player_one_name)
        print(self.player_one_chooses)

    def player_two(self):
        self.player_two_name = "David the Challenger"
        self.player_two_chooses = ['Spock', 'Rock', 'Scissors', 'Paper', 'Lizard']
        print(self.player_two_name)
        print(self.player_two_chooses)

