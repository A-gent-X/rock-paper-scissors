from Human import Human
from Computer import computer
from Players import Players



class Game:
    def __init__(self):
        self.Player = Players


    def set_Players(self):
        self.Players = input[Human, computer]
        print(self.Players)



def run():
    greeting()

def greeting():

    Welcome_greeting = "Welcome to a game of Ultimate risk!"
    print(Welcome_greeting, "Ultimate match of Rock, Paper and Scissors played on the next level!")

    Ultimate_rules = "Simple, each player must place all chips on chance, luck and strategy"
    print(Ultimate_rules, "Choose wisely, 1st to win 2 out of 3 rounds wins!")

    Ultimate_competitors = "This will be a contest between two robust competitors!"
    print(Ultimate_competitors, "Good luck to all challengers and leeeeeets the games begin!")


def run_game():

    while Game:
        if computer.chosen_gesture() > Human.chosen_gesture():
            print(computer, "wins!")
        if computer.chosen_gesture() < Human.chosen_gesture():
            print(Human, "is victorious!")
        if computer.chosen_gesture() == Human.chosen_gesture():
            print("It's look like we have a stale mate!")
        if computer.chosen_gesture() < Human.chosen_gesture():
            print("Human triumphs over machine this round!")















