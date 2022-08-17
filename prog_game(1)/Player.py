from Game import *
from Character import *

class Player :

    def __init__(self, name, life, money):
        self.name = name
        self.life = life
        self.money = money
        self.direction = None
        self.team = []

    @property
    def is_alive(self):
        return self.live > 0

    def get_hit(self, damages):
        """
        Take the damage to life
        PARAM : - damages : float
        """
        # TODO


    def new_character(self):
        """
        Ask to player where add a new Character,
        check if enough monney
        and create the new one
        """
        line = input(f"{self.name}: Wich line would you place the new one (0-{self.game.nb_lines-1}) ? (enter if none) ")
        if line != "":
            line = int(line)
            if 0<=line<=self.game.nb_lines-1 :
                if self.money >= Character.base_price :
                    column = 0 if self.direction == +1 else self.game.nb_columns-1
                    Character(self,(line,column))