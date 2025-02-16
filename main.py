import pygame,sys #imports the pygame module and the sys module
from simulation import Simulation #imports the simulation class
pygame.init() #inits pygame
pygame.mouse.set_visible(False) #hides the mouse cursor
WINDOW_WIDTH = 800 #sets window width
WINDOW_HEIGHT = 600 #sets window height
CELL_SIZE = 6 #defines the size of each cell on the grid
FPS = 1000000        #defines the FPS value
GREY = (29,29,29)  #sets the "GREY" value to the color code thing for grey


window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT)) # creates display surface object named window
pygame.display.set_caption("Falling Sand") #sets window title

clock = pygame.time.Clock() #controls frame rate
simulation = Simulation(WINDOW_WIDTH,WINDOW_HEIGHT,CELL_SIZE)

#Simulation Loop  #while loop runs continusly until window is closed
while True:


    # 1. Event Handling
    simulation.handle_controls()
    
    
    
    
    # 2. Updating State
    simulation.update()
    # 3. Drawing Grid
    window.fill(GREY) #Sets background color to the grey value
    simulation.draw(window) #calls the draw method
    pygame.display.flip() #takes all changes made in the simulation and draws picture from it
    clock.tick(FPS)       #sets the frame rate to the "FPS" value which is 120