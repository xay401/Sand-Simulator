#This class is reponsible for:
 #creating and manager the grid
 #adding & removing particles
 #coordinating the overal simulation

import pygame, sys, random
from grid import Grid #imports grid class
from particle import SandParticle #imports sand particle class
from particle import RockParticle #imports rock particle class

class Simulation:                #creates the simulation class
    def __init__(self, width, height, cell_size):
        self.grid = Grid(width, height, cell_size)
        self.cell_size = cell_size
        self.mode = "sand"
        self.brush_size = 4

    def handle_controls(self):
        for event in pygame.event.get(): #Stops while loop if window is closed
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self.handle_key(event)
        self.handle_mouse()       

    def handle_key(self, event):
        if event.key == pygame.K_SPACE:
            self.restart()
        elif event.key == pygame.K_s: #switches particle to sand particle when s is pressed
            print("Sand Mode")
            self.mode = "sand"   
        elif event.key == pygame.K_r: #switches particle to rock mode when r is pressed
            print("Rock Mode")
            self.mode = "rock"
        elif event.key == pygame.K_e: #switches to eraser mode if e key is pressed
            self.mode = "erase"
            print("Eraser mode")

    def handle_mouse(self):
        buttons = pygame.mouse.get_pressed() #detects when lmb is pressed
        if buttons[0]:
            pos = pygame.mouse.get_pos() #detects the position of the mouse
            row = pos[1] // self.cell_size
            column = pos[0] // self.cell_size
            self.apply_brush(row, column)

    def draw(self, window):              #draws the grid
        self.grid.draw(window)
        self.draw_brush(window)

    def add_particle(self, row, column):
        if self.mode == "sand" :
            if random.random() < 0.5:
                self.grid.add_particle(row, column, SandParticle)
        elif self.mode == "rock":
            self.grid.add_particle(row, column, RockParticle)
            

    def remove_particle(self, row, column):
        self.grid.remove_particle(row, column)
   
    def update(self):
        for row in range(self.grid.rows - 2, -1, -1):
            for column in range(self.grid.columns):
                particle = self.grid.get_cell(row, column)
                if isinstance(particle, SandParticle):
                    new_pos = particle.update(self.grid, row, column)
                    if new_pos != (row, column):
                        self.grid.set_cell(new_pos[0], new_pos[1], particle)
                        self.grid.remove_particle(row, column)

    def restart(self):
        self.grid.clear()

    def apply_brush(self, row, column):
        for r in range(self.brush_size):
            for c in range(self.brush_size):
                current_row = row + r
                current_col = column + c

                if self.mode == "erase":
                    self.grid.remove_particle(current_row, current_col)
                else:
                    self.add_particle(current_row, current_col)

    def draw_brush(self, window):
        mouse_pos = pygame.mouse.get_pos()
        column = mouse_pos[0] // self.cell_size
        row = mouse_pos[1] // self.cell_size

        brush_visual_size = self.brush_size * self.cell_size
        color = (255, 255, 255)

        if self.mode == "rock":
            color = (100, 100, 100)
        elif self.mode == "sand":
            color = (185, 142, 66)
        elif self.mode == "erase":
            color = (255, 105, 180)

        pygame.draw.rect(window, color, (column * self.cell_size, row * self.cell_size, brush_visual_size, brush_visual_size))
