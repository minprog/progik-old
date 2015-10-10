import pygame
import time
import sys

HEIGHT = 100
WIDTH = 100

SCALE = 10
SCREEN = pygame.display.set_mode((WIDTH*SCALE, HEIGHT*SCALE))

def create_blank():
    """Creates a HEIGHT x WIDTH list containing all zero's. The inner lists 
    will all be WIDTH long and the outer list will HEIGHT long."""
    #TODO

def get_cell(board, x, y):
    """Returns the game board at position x,y , this is 1 if the cell at that 
    position is alive and 0 if the cell is dead. If the x or y parameters are
    out of bounds (not valid coordinates), the function returns 0."""
    #TODO

def count_neighbours(board, x, y):
    """Counts the number of alive neighbours around the position x,y , including 
    diagonal neighbours. Does not include the cell itself."""
    #TODO

def update(board):
    """Creates a new board copy and applies the game rules to each cell using 
    the old board. Does not modify the old board. Returns the new board."""
    #TODO
    
def read_file(filename):
    """Reads a .cells file and returns a 2D list containing the pattern.
    O = Alive
    . = Dead
    ! = Comment, ignore this line"""
    #TODO

def create_from_file(filename):
    """Creates a new blank board, reads the pattern from file and places the 
    pattern in the center of the board. Returns the created board."""
    #TODO
            
def draw_game(board):
    """Draws the current game board to the SCREEN"""
    #Fill the screen with a white rectangle, so no old squares remain
    pygame.draw.rect(SCREEN, (255,255,255), pygame.Rect(0, 0, WIDTH*SCALE, 
                     HEIGHT*SCALE))
    #Repeat for each cell
    for x in range(WIDTH):
        for y in range(HEIGHT):
            #If the cell at x,y is 1, draw a black square
            if board[y][x] == 1:
                pygame.draw.rect(SCREEN, (0,0,0), pygame.Rect(x*SCALE, y*SCALE,
                                 SCALE, SCALE))
            #Draw a grey border square (part of the grid)
            pygame.draw.rect(SCREEN, (100,100,100), pygame.Rect(x*SCALE, 
                             y*SCALE, SCALE, SCALE), 1)
    #Update the display
    pygame.display.flip()

def play():
    """Runs the game loop.
    Draws the board of the game, waits 1/10 second and then updates the game
    board. Also handles keyboard and mouse inputs."""
    #Checks if a filename was entered when running the game
    if len(sys.argv) == 1:
        board = create_blank()
    else:
        board = create_from_file(sys.argv[1]+'.cells')
    
    pause = True
    while True:
        #Draw the game board and wait 1/10 seconds
        draw_game(board)
        time.sleep(0.1)
        
        #Get all new events from Pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                pause = not pause
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x = event.pos[0] / SCALE
                y = event.pos[1] / SCALE
                board[y][x] = (board[y][x] + 1) % 2
                
        #If the game is running, update the game board
        if not pause:
            board = update(board)

#Run the play function when the code is started
if __name__ == '__main__':
    play()

