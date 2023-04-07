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

def solve(subo):
    
    # print(subo)
    find = find_empty(subo)
    if not find:
        return True
    else:
        row, col = find
        
    for i in range(1,10):
        if valid(subo, i, (row, col)):
            subo[row][col] = i
            
            if solve(subo):
                return True
            
            subo[row][col] = 0
    return False

def valid(subo, num, position):
    #Check row
    for i in range(len(subo[0])):
        if subo[position[0]] [i] == num and position[1] != i: #In this we will check each element in the row and is it equal to num
            return False
        
    #Check column
    for i in range(len(subo[0])):
        if subo[i][position[1]] == num and position[0] != i: #In this also we will check the current each element or value
            return False
    #Check Box
    box_g = position[1] //3
    box_p = position[0] //3
    
    for i in range(box_p*3, box_p*3 + 3):
        for j in range(box_g*3, box_g*3 + 3):
            if subo[i][j] == num and (i,j) != position:
                return False
    return True
    
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
    return None

print_suduko_board(suduko_board)
solve(suduko_board)
print("________________________")
print_suduko_board(suduko_board)