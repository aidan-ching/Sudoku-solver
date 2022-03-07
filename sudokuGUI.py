from tkinter import Button
from turtle import clear
import pygame

pygame.font.init()

WIDTH,HEIGHT = 600,700

SUDOKU_HEIGHT = 600

FPS = 60

BLUE = (0, 145, 255)
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BUTTON_COLOR = (100,100,100)

HORIZONTAL_ONE = pygame.Rect(0, 200, WIDTH, 3)
HORIZONTAL_TWO = pygame.Rect(0, 400, WIDTH, 4)

VERTICAL_ONE = pygame.Rect(200, 0, 3, SUDOKU_HEIGHT)
VERTICAL_TWO = pygame.Rect(400, 0, 4, SUDOKU_HEIGHT)

BOTTOM_BORDER = pygame.Rect(0, SUDOKU_HEIGHT-5, WIDTH, 5)
TOP_BORDER = pygame.Rect(0, 0, WIDTH, 5)
LEFT_BORDER = pygame.Rect(0, 0, 5, SUDOKU_HEIGHT)
RIGHT_BORDER = pygame.Rect(WIDTH-5, 0, 5, SUDOKU_HEIGHT)

NUMBER_FONT = pygame.font.SysFont("arial", 30)
BUTTON_FONT = pygame.font.SysFont("Corbel", 30)
CLEAR_BUTTON = pygame.Rect(100, HEIGHT-70, 150, 50)
SOLVE_BUTTON = pygame.Rect(350, HEIGHT-70, 150, 50)
clear_text = BUTTON_FONT.render("Clear", 1, WHITE)
solve_text = BUTTON_FONT.render("Solve", 1, WHITE)

boxes = []
for a in range(0,9): #generating the grid
    for b in range(0,9):
        box = pygame.Rect(a*(594//9)+5, b*(594//9)+5, (594//9), (594//9))
        boxes.append(box)
        box.x


WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku Solver")


def solve(board):
    #find an empty space
    find = findEmpty(board)
    #pygame.time.delay(15)
    drawWindow(board, (9,9))

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

def drawWindow(board, highlight_location):
    WIN.fill(WHITE)
    #render font
    for y, i in enumerate(board, start=0):
        for x, j in enumerate(i, start=0):
            if j != 0:
                num = NUMBER_FONT.render(str(j), 1, BLACK)
                WIN.blit(num, (x*(594//9) + 30, y*(594//9) + 20))

    pygame.draw.rect(WIN, BLACK, BOTTOM_BORDER)
    pygame.draw.rect(WIN, BLACK, TOP_BORDER)
    pygame.draw.rect(WIN, BLACK, LEFT_BORDER)
    pygame.draw.rect(WIN, BLACK, RIGHT_BORDER)

    pygame.draw.rect(WIN, BLACK, VERTICAL_ONE)
    pygame.draw.rect(WIN, BLACK, VERTICAL_TWO)

    pygame.draw.rect(WIN, BLACK, HORIZONTAL_ONE)
    pygame.draw.rect(WIN, BLACK, HORIZONTAL_TWO)

    for box in boxes: #draw boxes
        if find_box((box.x, box.y)) == highlight_location:
            pygame.draw.rect(WIN, BLUE, box, 1)
        else:
            pygame.draw.rect(WIN, BLACK, box, 1)

    pygame.draw.rect(WIN, BUTTON_COLOR, CLEAR_BUTTON) #x,y,width,height
    pygame.draw.rect(WIN, BUTTON_COLOR, SOLVE_BUTTON) #x,y,width,height
    WIN.blit(clear_text, (CLEAR_BUTTON.x + (clear_text.get_width()//2)+10, CLEAR_BUTTON.y + 13))
    WIN.blit(solve_text, (SOLVE_BUTTON.x + (solve_text.get_width()//2)+10, SOLVE_BUTTON.y + 13))

    pygame.display.update()

def find_box(location):
    return (location[0]//(594//9), location[1]//(594//9))
    #x is: location[0]//(594//9)
    #y is: location[1]//(594//9)

def update_board(board, location, number):
    board[location[1]][location[0]] = number





def main():
    clock = pygame.time.Clock()
    run = True

    highlight_location = (9,9) #null event

    board = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]

    while run:
        clock.tick(FPS)
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CLEAR_BUTTON.x <= mouse[0] <= (CLEAR_BUTTON.x+CLEAR_BUTTON.width) and CLEAR_BUTTON.y <= mouse[1] <= (CLEAR_BUTTON.y+CLEAR_BUTTON.height):
                    for a in range(0,9): #generating the grid
                        for b in range(0,9):
                            board[a][b] = 0

            if event.type == pygame.KEYDOWN and highlight_location != (9,9):
                if event.key == pygame.K_1:
                    update_board(board, highlight_location, 1)
                elif event.key == pygame.K_2:
                    update_board(board, highlight_location, 2)
                elif event.key == pygame.K_3:
                    update_board(board, highlight_location, 3)
                elif event.key == pygame.K_4:
                    update_board(board, highlight_location, 4)
                elif event.key == pygame.K_5:
                    update_board(board, highlight_location, 5)
                elif event.key == pygame.K_6:
                    update_board(board, highlight_location, 6)
                elif event.key == pygame.K_7:
                    update_board(board, highlight_location, 7)
                elif event.key == pygame.K_8:
                    update_board(board, highlight_location, 8)
                elif event.key == pygame.K_9:
                    update_board(board, highlight_location, 9)
                elif event.key == pygame.K_0:
                    update_board(board, highlight_location, 0)
                elif event.key == pygame.K_ESCAPE:
                    highlight_location = (9,9)

            if event.type == pygame.MOUSEBUTTONDOWN: #solve
                if SOLVE_BUTTON.x <= mouse[0] <= (SOLVE_BUTTON.x+SOLVE_BUTTON.width) and SOLVE_BUTTON.y <= mouse[1] <= (SOLVE_BUTTON.y+SOLVE_BUTTON.height):
                    solve(board)
                if 0 <= mouse[0] <= WIDTH and 0 <= mouse[1] <= SUDOKU_HEIGHT: #highlighting a box selection
                    highlight_location = find_box(mouse)
                else:
                    highlight_location = (9,9)

    
        drawWindow(board, highlight_location)

    main()

if __name__ == "__main__":
    main()

