

X = [[0,0,0],[0,0,0],[0,0,0]]
O = [[0,0,0],[0,0,0],[0,0,0]]


def add_piece(grid, cord):
    """Update the grid after computer or user moves 
    
    Args:
        grid: a 3x3 list 
        cord: a 1x2 list, [x,y]
    """
    [x, y] = cord 
    grid[x][y] = 1 
    return grid 
    
def user_moves(X,O):
    """ask the user for the coordinate to play an X; if there is a piece, warn and ask again until there is no piece
    """
    x = input("what row (0-index)? ")
    y = input("what column (0-index)? ")
    
    # if [x,y] is a cell already occupied by an X or an O, ask the user again. 
    
    
    return [x,y]



def computer_moves(X, O):
    """return the coordinate that the computer wants to put an O on the grid. 
    """
    ...
    return [x,y]

def judge(X, O):
    """return 1 is the user won, -1 if the computer won, 0 if tie, and 100 if too early to call.  
    """

def ko(judgement):
    """Print messages at the end of the game to greet, or to comfort the player. 
    """
    if judgement is 1:
        print ("Good job. you won.")
    elif judgement is -1:
        print ("Sorry, you were defeated by the computer. ")

def print_board(X, O):
    """Print the board with X's and O's like this:
    
    XOX
    _O_
    _XO
    
    where underlines means unoccupied/unmarked cells. 
    
    """
    ...

def game():
    while True:
        print_board(X,O)
    
        [x,y] = user_moves() # ask the user to make a move 
        X = add_piece(grid, [x,y])  # update the board after user moves

        judgement = judge(X,O)  # judge whether the game ends 
        if judgement is not 100:  # if the game is over
            ko(judgement) # print ending message
            return judgement ## game over, exit the function 
        
        [x,y] = computer_moves(X, O) # ask the computer to make a move
        O = add_piece(grid, [x,y])  # update the board after computer moves
        
        judgement = judge(X,O)  # judge whether the game ends 
        if judgement is not 100:  # if the game is over
            ko(judgement) # print ending message
            return judgement ## game over, exit the function 




if __name__ == "__main__":
    game()

