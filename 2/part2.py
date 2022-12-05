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
    
    def get_win(self):
        return Paper()
    
    def get_tie(self):
        return Rock()
    
    def get_loss(self):
        return Scissors()

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
    
    def get_win(self):
        return Scissors()
    
    def get_tie(self):
        return Paper()
    
    def get_loss(self):
        return Rock()

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
    
    def get_win(self):
        return Rock()
    
    def get_tie(self):
        return Scissors()
    
    def get_loss(self):
        return Paper()

def get_opponent_rps(rps_text):
    noramlized_text = rps_text.lower()
    if(noramlized_text == "a"):
        return Rock()
    elif(noramlized_text == "b"):
        return Paper()
    elif(noramlized_text == "c"):
        return Scissors()

def get_my_rps(opponent, rps_text):
    normalized_text = rps_text.lower()
    if(normalized_text == "x"):
        return opponent.get_loss()
    if(normalized_text == "y"):
        return opponent.get_tie()
    if(normalized_text == "z"):
        return opponent.get_win()

file = open(os.path.realpath(os.path.dirname(__file__)) + "\input.txt")

fileLines = file.read().splitlines()

#array of tuples of rps class for (your play, their play)
games = []

for x in fileLines:
    plays = x.split(' ')
    them = get_opponent_rps(plays[0])
    you = get_my_rps(them, plays[1])
    games.append((you, them))

tally = 0

for round in games:
    tally = tally + round[0].points
    tally = tally + round[0].play(round[1])

print(tally)
