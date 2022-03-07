import pprint

def solve(board):
    #find an empty space
    find = findEmpty(board)

    if find == False:
        return True


    if (find[0] == 8 and find[1] == 9):
        return True

    for i in range(1,10):
        if valid(board, find, i):
            board[find[0]][find[1]] = i
            if solve(board):
                return True
            
            board[find[0]][find[1]] = 0
    return False



def findEmpty(board):
    for x in range(len(board)):
        for y in range(len(board[x])):
            if (board[x][y] == 0):
                return x,y
    
    return False

def valid(board, position, number):
    #check row and column
    for i in range(9):
        if board[position[0]][i] == number:
            return False

    for i in range(9):
        if board[i][position[1]] == number:
            return False

    #check box
    a = position[0] - position[0]%3
    b = position[1] - position[1]%3

    for x in range(3):
        for y in range(3):
            if board[x + a][y + b] == number:
                return False

    return True



     



board2 = [[0,6,1,0,0,0,0,0,0],
          [3,5,2,1,6,8,7,4,9],
          [4,9,7,0,5,3,1,8,6],
          [2,1,8,9,0,5,6,3,4],
          [0,7,5,3,4,1,9,0,8],
          [9,3,4,6,8,2,0,1,7],
          [5,0,6,8,1,9,0,7,3],
          [7,0,3,0,2,6,0,9,1],
          [1,8,9,4,3,7,2,6,5]]

grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]

empty = [[0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]]

pp = pprint.PrettyPrinter(width = 41, compact=True)

#pp.pprint(board)


solve(board2)

pp.pprint(board2)

solve(grid)

pp.pprint(grid)

solve(empty)
pp.pprint(empty)