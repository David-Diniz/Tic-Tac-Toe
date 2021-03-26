import pygame, sys#imports pygame
import numpy as np

pygame.init()#initializes pygame, allowing us to use it


for i in range(5):
    print('')
print('Hello and welcome to Tic Tac Toe made by David Diniz, if at any point you would like to restart, simply press r')

WIDTH = 600
HEIGHT = 600
BOARD_ROWS = 3
BOARD_COLS = 3
LINE_COLOUR=(255,243,5)
LINE_WIDTH =(15)
xColour = (255,0,0)
oColour = (0,0,255)
circleRadius = 60
circleWidth = 15
xWidth = 10
SPACE = 50
Black = (0,0,0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TIC TAC TOE')#sets the window to be named tic tac toe


board = np.zeros((BOARD_ROWS, BOARD_COLS))#This creates what i would dare to call a boolean board, i will use it for various checks

def draw_figures(): #this function will actually draw the x's and o's on the board
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] ==1: #this if statement determines whether or not it is player one's turn
                pygame.draw.circle(screen, oColour, (int(col * 200 + 100), int(row * 200 + 100)), circleRadius, circleWidth) #draws a circle in the chosen square
            elif board[row][col] ==2: #determines whether it is player two's turn
                #the next two lines draw an X in the chosen box
                pygame.draw.line(screen, xColour, (col*200 + SPACE, row*200 + 200 - SPACE), (col* 200 +200 - SPACE, row*200 +SPACE), xWidth)
                pygame.draw.line(screen, xColour, (col * 200 + SPACE, row * 200 + SPACE), ( col * 200 + 200 - SPACE, row * 200 + 200 - SPACE), xWidth)
                
def draw_lines():#this entire function will draw our tic tac toe grid for us
    #1 horizontal
    pygame.draw.line(screen, LINE_COLOUR, (0,200), (600,200), LINE_WIDTH)
    #2 Horizontal
    pygame.draw.line(screen, LINE_COLOUR, (0,400), (600, 400), LINE_WIDTH)
    #1 vertical
    pygame.draw.line(screen, LINE_COLOUR, (200,0), (200,600), LINE_WIDTH)
    #2 VERTICAL
    pygame.draw.line(screen, LINE_COLOUR, (400,0), (400,600), LINE_WIDTH)

def mark_square(row, col, player):
#this will mark our board and tell us which player is in which square    
    board[row][col] = player

def available_square(row,col):
    #this function checks if a certain square is available
    if board[row][col] == 0: #checks if a square has value 0, if it does then its available
        return True
    else: #anything other than a zero and it is taken so ot returns false
        return False
    
def is_board_full(): #this will check if the board is full
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):#two for loops will go through and check each cell and tell us if it is full or not
            if board[row][col] == 0:
                return False #if not all cells are full than the function returns False
    return True #only other option is its full and so it then returns True

def check_win(player):
    #vertical win check
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_win_line(col, player)
            return True
    #horizontal win check
    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_win_line(row, player)
            return True
    #asc diagonal win check
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diagonal(player)
        return True
    #desc diagonal line
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc_diagonal(player)
        return True

    return False

def draw_vertical_win_line(col, player):
    posX = col*200 + 100
    if player ==1:
        colour = oColour
    elif player == 2:
        colour = xColour
    pygame.draw.line(screen, colour, (posX, 50), (posX, 550), 5)   
def draw_horizontal_win_line(row,player):
    posY = row*200 + 100
    if player == 1:
        colour = oColour
    elif player == 2:
        colour = xColour
    pygame.draw.line(screen, colour, (50, posY), (550, posY), 5)
def draw_asc_diagonal(player):
    if player ==1:
        colour = oColour
    elif player ==2:
        colour = xColour
    pygame.draw.line(screen, colour, (50,550), (550,50), 5)
def draw_desc_diagonal(player):
    if player == 1:
        colour = oColour
    elif player == 2:
        colour = xColour
    pygame.draw.line(screen, colour, (50,50), (550,550), 5)
def restart():
    screen.fill(Black)
    draw_lines()
    player = 2
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0

draw_lines()

player = 1
gameOver = False

#mainloop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not gameOver: 

            mouseX = event.pos[0] #x coordinate, reads the x coordinate of your mouse click
            mouseY = event.pos[1] #y coordinate, reads the y coordinate of your mouse click
#these two lines identify where the mouse was clicked and sets it relative to my grid, a row or column equal to 1,2 or 3
            clicked_row = int(mouseY // 200)
            clicked_col = int(mouseX // 200)
            
            if available_square(clicked_row, clicked_col): #checks if the square that was clicked is availbale
                
                if player == 1: #checks if the player is one, if it is, this happens
                    mark_square(clicked_row, clicked_col, 1)#calls the mark square function to claim this square in the name of player 1
                    if check_win(player):
                        gameOver = True
                    player = 2 #sets player to two because if player one just went, then it is now player two's turn
                    
                elif player == 2: #this elif does the same thing but for player #2
                    mark_square(clicked_row, clicked_col, 2)
                    if check_win(player):
                        gameOver = True
                    player = 1
                
                draw_figures()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                gameOver = False
                
    pygame.display.update()

















    
