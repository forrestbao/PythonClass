

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
    
    
    return X



def computer_moves(X, O, counterX, counterY):
    """return the coordinate that the computer wants to put an O on the grid. 
    """
    
    randomX, counterX = cyrandom(counterX)
    randomY, counterY = cyrandom(counterX)
    
    # use a while here, if the coordinate (randomX, randomY) is occupied.
    
    ...
    return X, counterX, counteY 

def judge(X, O):
    """return 1 is the user won, -1 if the computer won, 0 if tie, and 100 if too early to call.  
    """

def ko(judgement):
    """Print messages at the end of the game to greet, or to comfort the player. 
    
    judgment:
    1: tie
    2: computer wins
    3: human wins
    
    """
    if judgement==3:
        print ("Good job. you won.")
    elif judgement == 2:
        print ("Sorry, you were defeated by the computer. ")

def print_board(X, O):
    """Print the board with X's and O's like this:
    
    XOX
    _O_
    _XO
    
    where underlines means unoccupied/unmarked cells. 
    
    """
    ...

def cyrandom(counter):
    L = [1,2,3]
    draw = L[counter]
    counter += 1 
    return draw, counter 
    
def game():
    counterX, counterY = 0, 2
    while True:
        print_board(X,O)
    
        O = user_moves(X, O) # ask the user to make a move 

        judgement = judge(X,O)  # judge whether the game ends 
        if judgement < 4:
            ko(judgement)
            return 0
       
        X, counterX, counterY = computer_moves(X, O, counterX, counterY) # ask the computer to make a move
        
        judgement = judge(X,O)  # judge whether the game ends 
        if judgement < 4:
            ko(judgement)
            return 0

if __name__ == "__main__":
    game()

