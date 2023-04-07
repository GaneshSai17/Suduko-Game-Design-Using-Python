suduko_board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def print_suduko_board(subo):
    for i in range (len(subo)):
        if i % 3 == 0 and i !=0:
            print("- - - - - - - - - -") 
        
        for j in range(len(subo[0])):
            if j % 3 == 0 and j !=0:
                print("|", end = "")
                
            if j == 8:
                print(subo[i][j])
            else:
                print(str(subo[i][j]) + " ", end="")
print_suduko_board(suduko_board)

def find_empty(subo):
    for i in range(len(subo)):
        for j in range(len(subo[0])):
            if subo[i][j] == 0:
                return (i,j) #row Col