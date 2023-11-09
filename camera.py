import pygame

class Camera:
    def __init__(self, pos):
        super().__init__()
        self.pos = pos
        self.width = 1024
        self.focus = None

    def set_focus(self, object_to_focus):
        self.focus = object_to_focus

    def move(self, dir):
        self.pos = self.pos+ dir