from Player import human_player, computer_player
import time

class TicTacToe:
    def __init__(self):
        self.board= [' ' for _ in range(9)] #this list represents a 3x3 board 
        self.current_winner = None #to keep track of the winner

    def print_board(self):
        #this is just getting rows in the form (0,1,2)
        #                                     ,(3,4,5)
        #                                     ,(6,7,8)
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print ('| ' + ' | ' .join(row)+' |')

    @staticmethod
    def print_board_number():
        #this method prints a board with the indices
        #this number shows which number corresponds to what box
        number_board= [[str(i) for i in range(j*3,(j+1)*3)] for j in range(3)] #range(j*3:(j+1)*3) for j in range(3)

        for row in number_board:
            print ('| ' + ' | ' .join(row)+' |')
    
    def available_moves(self):
        # to keep a track of how many squares are empty
        return[ i for i, spot in enumerate(self.board) if spot==' ']   
    
    def empty_squares(self):
        # just checks if there is a empty square
        return ' ' in self.board #returns a boolean value
    
    def number_of_empty_squares(self):
        # returns no of empty squares
        return len(self.available_moves())    

    def make_move(self, square, letter):
        if self.board[square]==' ':           #this method makes a move, checks the validity 
            self.board[square]=letter         #of the move and also checks if the is a winner.
            if self.Winner(square,letter):
                self.current_winner=letter
            return True
        return False
    
    def Winner(self, square, letter):
        # this method checks for the winning condition
        
        # first we check for rows
        row_ind = square // 3                       #returns the quotient, so the possible answwers are 0,1,2         
        row = self.board[row_ind*3 : (row_ind+1) * 3]
        if all(spot == letter for spot in row):
            return True
        
        # Now we check for columns        
        col_ind = square%3
        col=[self.board[col_ind+i*3] for i in range(3)]
        if all(spot == letter for spot in col):
            return True
        
        # And finally we check for the diagonals
        # as there are only two possible outcomes we check directly for them
        if square%2==0:
            diagonal1= [self.board[i] for i in [0,4,8]]
            if all(spot == letter for spot in diagonal1):
                return True
            diagonal2= [self.board[i] for i in [2,4,6]]
            if all(spot == letter for spot in diagonal2):
                return True
        
        return False

def play(game, X_player, O_player, print_game=True):
    if print_game:
        game.print_board_number()
    letter = 'X' 
    while game.empty_squares():       # This loop will run till all the squares are filled 
        if letter == 'O':             # get the square where the move is to be made
            square=O_player.get_move(game)
        else:
            square= X_player.get_move(game)
        
        if game.make_move(square,letter):
            if print_game:
                print(letter + f'makes a move to square {square}')
                game.print_board()  
                print(' ')

            if game.current_winner:
                if print_game:
                    print(letter + ' winns!!!!')
                return letter
           
            letter = 'O' if letter == 'X' else 'X'   #to alternate move
            time.sleep(1.5)
        
    if print_game:
       print("It's a tie!")

if __name__ == '__main__':
    X_player = human_player('X')
    O_player = computer_player('O')
    t=TicTacToe()
    play(t, X_player, O_player, print_game = True)