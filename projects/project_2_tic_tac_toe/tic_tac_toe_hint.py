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
        

X = [[1,0,0],[0,0,0],[0,1,0]]
O = [[0,1,0],[0,1,0],[0,0,1]]

print_grid(X, O )


