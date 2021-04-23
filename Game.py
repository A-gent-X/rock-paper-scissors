from Human import Human
from Computer import computer
from Players import Players
from Gestures import gestures


class Game:
    def __init__(self):
        self.Player = Players
        self.gestures = gestures

    def set_Players(self):
        self.Players = input[Human, computer]
        print(self.Players)

    def set_Gestures(self):
        self.gestures = input(gestures)
        print(self.gestures)

def run():
    greeting()

def greeting():

    Welcome_greeting = "Welcome to a game of Ultimate risk!"
    print(Welcome_greeting, "Ultimate match of Rock, Paper and Scissors played on the next level!")

    Ultimate_rules = "Simple, each player must place all chips on chance, luck and strategy"
    print(Ultimate_rules, "Choose wisely, 1st to win 2 out of 3 rounds wins!")

    Ultimate_competitors = "This will be a contest between two robust competitors!"
    print(Ultimate_competitors, "Good luck to all challengers and leeeeeets the games begin!")

while Game:
    if Human.chosen_gesture() > computer.gesture_list():
        break

#     print("PlayerAI wins the round!")
# elif PlayerOne.Lizard > PlayerAI.Paper:
#     print("PlayerAI is the victor!")
# else:
#     print("PlayerAI claims this round!")
#
# if PlayerOne.Paper < PlayerAI.Spock:
#     print("PlayerOne wins!")
# elif PlayerOne.Lizard < PlayerAI.Paper:
#     print("PlayerOne takes the win!")
# else:
#     print("PaperOne is victor lets begin final round!")
#
# if PlayerOne.Scissors < PlayerAI.Paper:
#     print("PlayerAI takes the round!")
# elif PlayerOne.Spock < PlayerAI.Rock:
#     print("PlayerOne is the victor!")
# else:
#     print("PaperOne won 2 out of 3 Brock is victorious!")
#
#
# if PlayerOne.Paper < PlayerTwo.Spock:
#     print("PlayerOne wins the round!")
# elif PlayerOne.Spock < PlayerTwo.Rock:
#     print("PlayerOne is victor!")
# else:
#     print("PaperOne win round 1!")
#
# if PlayerOne.Scissors > PlayerTwo.Rock:
#     print("Player wins the round!")
# elif PlayerOne.Paper > PlayerTwo.Lizard:
#     print("PlayerOne is the victor!")
# else:
#     print("PaperOne tekes round 2!")
#
# if PlayerOne.Lizard < PlayerTwo.Spock:
#     print("Player wins the round!")
# elif PlayerOne.Rock > PlayerTwo.Paper:
#     print("PlayerOne is the victor!")
# elif PlayerOne.Scissors < PlayerTwo.Rock:
#     print("PlayerTwo wins!")
# else:
#     print("PaperTwo is the Ultimate Champion!")
#
#
#





#    Objective is finding a way to display game rules
#    Who is playing the game?
#    Start the game
#    Each player has to select the gesture
#    Compare the gestures(see what gesture each player picked)
#    Who is the victor or if there is a tie?
#    Each players needs to be able hold a gestures










