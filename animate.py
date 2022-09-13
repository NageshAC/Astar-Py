import pygame
from Grid import Grid

ORDER = (60,100)
WIDTH = 20


def main(win):

    start = None
    end  = None
    run = True

    grid = Grid(ORDER, WIDTH)
    grid.draw(win)

    while run:
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

            # Left Mouse Botton -> set Node
            if pygame.mouse.get_pressed()[0]: # Left Mouse Botton

                pos = pygame.mouse.get_pos()
                pos = (pos[1]//WIDTH, pos[0]//WIDTH)

                type = None
                if not start and not grid.grid[pos].is_end(): 
                    type = 'SRC'
                    start = pos

                elif not end and not grid.grid[pos].is_start(): 
                    type = 'DEST'
                    end = pos
                elif grid.grid[pos].is_empty():
                    type = 'WALL' 

                if type != None:   
                    grid.grid[pos].cngColor(type)
                
                grid.grid[pos].draw(win)
                pygame.display.update()
            
            # Right Mouse Botton -> reset node
            if pygame.mouse.get_pressed()[2]: 

                pos = pygame.mouse.get_pos()
                pos = (pos[1]//WIDTH, pos[0]//WIDTH)

                if 0 in pos or ORDER[0]-1 in pos or ORDER[1]-1 in pos:
                    continue
                type = 'EMT'
                
                if grid.grid[pos].is_start():
                    start = None
                if grid.grid[pos].is_end():
                    end = None
                
                grid.grid[pos].cngColor(type)
                grid.grid[pos].draw(win)
                pygame.display.update()

            if event.type == pygame.KEYDOWN:
                # Enter key -> Reset
                if event.key == pygame.K_RETURN:
                    
                    start, end  = None, None
                    set_start, set_end = False, False

                    grid = Grid(ORDER, WIDTH)
                    grid.draw(win)

                # Space Bar -> Start the game
                if event.key == pygame.K_SPACE:
                    if not grid.solve(win):
                        print('No route possible')

                


    pygame.quit()

if __name__ == '__main__': 
    RES = (ORDER[1]*WIDTH,ORDER[0]*WIDTH)
    WIN = pygame.display.set_mode(RES)
    pygame.display.set_caption('A* Path Finding Algorithm')
    
    main(WIN)