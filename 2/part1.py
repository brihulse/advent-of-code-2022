import os

class Rock:
    def __init__(self):
        self.points = 1
    
    def play(self, opponent_rps):
        if(isinstance(opponent_rps, Rock)):
            return 3
        elif(isinstance(opponent_rps, Paper)):
            return 0
        elif(isinstance(opponent_rps, Scissors)):
            return 6
    
class Paper:
    def __init__(self):
        self.points = 2
    
    def play(self, opponent_rps):
        if(isinstance(opponent_rps, Rock)):
            return 6
        elif(isinstance(opponent_rps, Paper)):
            return 3
        elif(isinstance(opponent_rps, Scissors)):
            return 0

class Scissors:
    def __init__(self):
        self.points = 3
    
    def play(self, opponent_rps):
        if(isinstance(opponent_rps, Rock)):
            return 0
        elif(isinstance(opponent_rps, Paper)):
            return 6
        elif(isinstance(opponent_rps, Scissors)):
            return 3

def get_rps(rps_text):
    noramlized_text = rps_text.lower()
    if(noramlized_text == "a" or noramlized_text == "x"):
        return Rock()
    elif(noramlized_text == "b" or noramlized_text == "y"):
        return Paper()
    elif(noramlized_text == "c" or noramlized_text == "z"):
        return Scissors()

file = open(os.path.realpath(os.path.dirname(__file__)) + "\input.txt")

fileLines = file.read().splitlines()

#array of tuples of rps class for (your play, their play)
games = []

for x in fileLines:
    plays = x.split(' ')
    them = get_rps(plays[0])
    you = get_rps(plays[1])
    games.append((you, them))

tally = 0

for round in games:
    tally = tally + round[0].points
    tally = tally + round[0].play(round[1])

print(tally)
