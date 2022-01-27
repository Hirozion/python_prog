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
        print(self.secret) #just for testing remove for playing when over

    def gamemode(self):
        match self.gm:
            case 1: #solo
                self.gm = 1
            case 2: #TODO: vs IA a deff
                self.gm = 2
    
    def gameplay(self):
        while True:
            print("** -- Life Player {0} -- **".format(self.p.life))
            self.p.play()
            if self.p.choice == self.secret:
                print("GG !")
                exit(1)
            elif self.p.life == 0:
                print(" -- Game Over L")
                exit(1)
            else:
                self.p.life -= 1
        
class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.life = 5
        self.choice = None
    def play(self):
        self.choice = int(input("Rentrez un nombre svp : ")) #toupdate handling error
        
if __name__ == "__main__":
    P1 = Player("Martin")
    G1 = Game(1,1,P1)
    G1.choiceDifficulty()
    G1.gameplay()






"""
# a simple game make a class 
# with this add difficulty lvl 1 - 2 -3 
# and play simply play the game
# add life 
# add solo or vs IA hardOne
#   
"""