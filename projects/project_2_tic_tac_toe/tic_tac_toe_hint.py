def print_grid(X,O):
    """print the board wit X's, O's and underlines to visualize the state of the board 
    
    
    args:
        X: a list of 3-element sublists of 1's and 0's
        O: a list of 3-element sublists of 1's and 0'
        
    note:
        A 1 in X or means an X or O in the corresponding cell in the grid. 0 if no X nor O in the corresponding cell 
        For example, given the layout 
        XOX
        _O_
        _XO
        
        X will be [[1,0,1],[0,0,0],[0,1,0]]
        O will be [[0,1,0],[0,1,0],[0,0,1]]
        
    """
    for i in range(3): # row index
        Row = "" 
        for j in range(3):  # column index
            if X[i][j] is 1:
                Row += "X"
            elif O[i][j] is 1:
                Row += "O"
            else:
                Row += "_" 
        print (Row )
        

X = [[1,0,0],[0,0,0],[0,1,0]]
O = [[0,1,0],[0,1,0],[0,0,1]]

"""
import hw5_hint2

[x,y] = hw5_hint2.user_moves()
print_grid(X,O) 
"""
