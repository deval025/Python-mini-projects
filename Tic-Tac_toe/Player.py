import random as rand
import math

from numpy import square

class player:
    def __init__(self, letter):
        #letter is X or O
        self.letter = letter
    
    # to alternate move 
    def get_move(self, game):
        pass

class computer_player(player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):                            #picks a random square from the available moves
        square = rand.choice(game.available_moves())
        return square

class human_player(player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        valid_square=False
        val =None
        # the loop will run till a valid square is entered by the user
        while not valid_square:
            square = input(self.letter + "'s turn. tnput move(0-8)")
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square=True
            except ValueError:
                print("invalid square. Enter a valid value")
        return val

