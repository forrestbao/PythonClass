    
def user_moves(X,O):
    """ask the user for the coordinate to place an O; if there is a piece, warn and ask again until there is no piece
    """
    x = input("what row (0-index)? ")
    y = input("what column (0-index)? ")
    
    # add a while-loop here, as long as (x,y) is occupied by an X or an O, ask again. 


    return X

def computer_moves(X, O, counterX, counterY):
    """
    Let the computer randomly choose a cell on the grid to put an X. The new location must be unoccupied.  
    """
    
    randomX, counterX = cyrandom(counterX)
    randomY, counterY = cyrandom(counterX)
    
    # add a while-loop here, as long as the random coordinate (randomX, randomY) is occupied by an X or an O, regenerate.
    
    return X, counterX, counteY 

def judge(X, O):
    """
    Based on the lists X and O, return one of the following judgments:
    1: tie
    2: computer (playing X) wins
    3: human (playing O) wins
    4: else (the game should keep going )

    """

def ko(judgement):
    """Print messages at the end of the game to greet, or to comfort the player. 
    
    judgment:
    1: tie
    2: computer (playing X) wins
    3: human (playing O) wins
    4: else (the game should keep going )
    
    """
    if judgement==3:
        print ("Good job. you won.")
    elif judgement == 2:
        print ("Sorry, you were defeated by the computer. ")

    # add code here to finish the cases 

def print_grid(X,O):
    """print the board wit X's, O's and underlines to visualize the state of the board 
    
    
    args:
        X: a list of 3-element sublists of 1's and 0's
        O: a list of 3-element sublists of 1's and 0's
        
    note:
        A 1 in X or means an X or O in the corresponding cell in the grid. 0 if no X nor O in the corresponding cell 
        For example, given the layout 
        XOX
        _O_
        _XO
        
        X will be [[1,0,1],[0,0,0],[0,1,0]], and 
        O will be [[0,1,0],[0,1,0],[0,0,1]]
        
    """
   
    for row in range(3):
        Lthisrow = ""
        for column in range(3):
            if X[row][column] == 1:
                Lthisrow += "X"
            elif O[row][column] == 1:
                Lthisrow += "O"
            else:
                Lthisrow += "_"
        print (Lthisrow)
                
    return None  

def cyrandom(counter):
    """A simple random number generator 

    It draws an element from the list L below based on the counter.
    The counter advances by 1 after the drawing. 
    If the new counter is greater than 2, reset it to 0. 

    """

    L = [0,1,2]
    draw = L[counter]
    counter += 1 

    # add your code here to reset the counter to 0 if counter is greater than 2 


    return draw, counter 
    
def game(X, O):
    """This function is complete. No need to modify. 
    """

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

# feel free to call any functions above under this line 
if __name__ == "__main__":

    X = [[0,0,0],[0,0,0],[0,0,0]]
    O = [[0,0,0],[0,0,0],[0,0,0]]
    game(X, O )

