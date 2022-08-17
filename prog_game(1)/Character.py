### PERSONNAGES ###
class Character :

    base_price = 1
    base_life = 5
    base_strength = 1 

    def __init__(self, player, position):
        """
        PARAM : - player : Player
                - position : tuple
        Set player to player in param.
        Set life, strength and price to base_life, base_strength and base_price.
        Place th character at the position
        If OK : add the current character to the player's team and take the price
        """

        self.player = player
        self.life = self.base_life
        self.strength = self.base_strength
        self.price = self.base_price

        ok = self.game.place_character(self, position)
        if ok :
            self.player.team.append(self)
            self.player.money -= self.price


    @property
    def direction(self):
        # TODO
        return 0

    @property
    def game(self):
        # TODO
        return 0

    @property
    def enemy(self):
        # TODO
        return 0

    @property
    def design(self):
        # TODO
        return 0


    def move(self):
        """
        the character move one step front
        """
        # TODO


    def get_hit(self, damages):
        """
        Take the damage to life. If dead, the character is removed from his team and return reward
        PARAM : damages : float
        RETURN : the reward due to hit (half of price if the character is killed, 0 if not)
        """
        # TODO


    def attack(self):
        """
        Make an attack :
            - if in front of ennemy's base : hit the base
            - if in front of character : hit him (and get reward)
        """
        # TODO


    def play_turn(self):
        """
        play one turn : move and attack
        """
        # TODO


    def __str__(self):
        """
        return a string represent the current object
        """
        # TODO
