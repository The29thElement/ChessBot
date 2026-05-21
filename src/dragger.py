import pygame

from const import *

class Dragger:
    
    def __init__(self):
        self.mouseX = 0.0
        self.mouseY = 0.0
        self.inital_row = 0

    def update_mouse(self, pos):
        self.mouseX, self.mouseY = pos # (x, y)

    def save_initial(self, pos):
        pass