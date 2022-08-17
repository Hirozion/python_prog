class Game :

    def __init__(self,player0, player1, nb_lines=6,nb_columns=15):
        """
        PARAM : - player0 : Player
                - player1 : Player
                - nb_lines : float
                - nb_columns : float
        - update players' direction and game
        - initialisate player_turn to 0
        """
        # TODO


    @property
    def current_player(self):
        # TODO
        return 0

    @property
    def oponent(self):
        # TODO
        return 0

    @property
    def all_characters(self):
        # TODO
        return 0


    def get_character_at(self, position):
        """
        PARAM : - position : tuple
        RETURN : character at the position, None if there is nobody
        """
        # TODO


    def place_character(self, character, position):
        """
        place character to position if possible
        PARAM : - character : Character
                - position : tuple
        RETURN : bool to say if placing is done or not
        """
        # TODO



    def draw(self):
        """
        print the board
        """
        print(f"{self.players[0].life:<4}{'  '*self.nb_columns}{self.players[1].life:>4}")

        print("----"+self.nb_columns*"--"+"----")

        for line in range(self.nb_lines):
            print(f"|{line:>2}|", end="")
            for col in range(self.nb_columns):
                # TODO
                print(".", end=" ")
            print(f"|{line:<2}|")

        print("----"+self.nb_columns*"--"+"----")

        print(f"{self.players[0].money:<3}${'  '*self.nb_columns}${self.players[1].money:>3}")


    def play_turn(self):
        """
        play one turn :
            - current player can add a new character
            - current player's character play turn
            - oponent player's character play turn
            - draw the board
        """
        # TODO



    def play(self):
        """
        play an entire game : while current player is alive, play a turn and change player turn
        """
        # TODO
