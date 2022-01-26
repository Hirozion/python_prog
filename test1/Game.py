import random

class Game:
    def __init__(self, difficulty, gamemode, player) -> None:
        self.diff = difficulty
        self.gm = gamemode
        self.p = player
        self.secret = None
    def choiceDifficulty(self):
        match self.diff:
            case 1:
                self.secret = random.randint(0,10)
            case 2: 
                self.secret = random.randint(0,20)
            case 3: 
                self.secret = random.randint(0,50)
    def gamemode(self):
        match self.gm:
            case 1: #solo
                self.gm = 1
            case 2: #TODO: vs IA a deff
                self.gm = 2
    
    def gameplay(self):
        pass
class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.life = 5
        self.choice = None
    def play(self):
        self.choice = int(input("Rentrez un nombre svp : ")) #toupdate handling error

P1 = Player("Martin")
P1.play()
"""
secret = random.randint(0,10)
life = 3

print(secret)
nb = int(input("Rentrez un nombre svp : "))

while True:
    if nb == secret:
        print("GG !")
        exit(1)
    elif life == 0:
        print(" -- Game Over L")
        exit(1)
    else:
        nb = int(input("Rentrez un nombre svp : "))
        life -= 1

# a simple game make a class 
# with this add difficulty lvl 1 - 2 -3 
# and play simply play the game
# add life 
# add solo or vs IA hardOne
#   
"""