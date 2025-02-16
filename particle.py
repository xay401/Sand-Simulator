import random #imports the random module
import colorsys #imports the colorsys module



class SandParticle:                  #creats sand particle class
     def __init__(self):
          self.color = random_color((0.1,0.12),(0.5,0.7),(0.7,0.9))             #sets sand particle color to random color

     
     def update(self,grid,row,column):
            if grid.is_cell_empty(row + 1,column):
              return row + 1,column
            else:
                offsets = [-1,1]
                random.shuffle(offsets)
                for offset in offsets:
                     new_column = column + offset
                     if grid.is_cell_empty(row +1,new_column):
                          return row + 1,new_column
                     
            return row,column         








class RockParticle:
     def __init__(self):
          self.color = random_color((0.0,0.1),(0.1,0.3),(0.3,0.5))

def random_color(hue_range,saturation_range,value_range):
     hue = random.uniform(*hue_range)
     saturation = random.uniform(*saturation_range)
     value = random.uniform(*value_range)
     r,g,b = colorsys.hsv_to_rgb(hue,saturation,value) #converts the hsv color values to rgb color values
     return int(r*255), int(g*255),int(b*255) #returns the converted values