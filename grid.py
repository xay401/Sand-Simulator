#Making the grid
import pygame #imports pygame module
LIGHT_GREY = (55,55,55) #defines the light grey value as the light grey color code thing
class Grid:                 #creates the grid class
    def __init__(self,width,height,cell_size):
        self.rows = height // cell_size
        self.columns = width // cell_size
        self.cell_size = cell_size
        self.cells = [[None for _ in range(self.columns)] for _ in range(self.rows)] #generates the grid and fills all the cells with none(absense of any data/value)


    def draw(self,window): #defines the draw command
        for row in range(self.rows):
            for column in range(self.columns):
                color = LIGHT_GREY
                particle = self.cells[row][column]
                if particle is not None:
                    color = particle.color
                pygame.draw.rect(window,color,
                     (column * self.cell_size, row * self.cell_size,self.cell_size,self.cell_size))
    def add_particle(self,row,column,particle_type):
        if 0 <= row < self.rows and 0 <= column < self.columns and self.is_cell_empty(row,column):
             self.cells[row][column] = particle_type() #particle type is a paramter that allows specification of what type of particle to add to the grid
    def remove_particle(self,row,column):
        if 0 <= row < self.rows and 0 <= column < self.columns:
             self.cells[row][column] = None
    def is_cell_empty(self,row,column):
        if 0 <= row < self.rows and 0 <= column < self.columns:
            if self.cells[row][column] is None:
                return True
        return False
    def set_cell(self,row,column,particle):
        if not(0 <= row < self.rows and 0 <= column < self.columns):
            return
        self.cells[row][column] = particle
    def get_cell(self,row,column):
        if 0 <= row < self.rows and 0 <= column < self.columns:
            return self.cells[row][column]
        return None
    def clear(self):
        for row in range(self.rows):
            for column in range(self.columns):
                self.remove_particle(row,column)