import pygame
import time
import random
import sys
from pygame import mixer
pygame.init()

width = 900
height = 600
surf = pygame.display.set_mode((width,height))

def draw_stars():
    class Star:
        def __init__(self):
            self.x = random.randint(-width ,width)
            self.y = random.randint(-height ,height)
            self.z = random.randint(-width ,width)
        
        def draw(self ,win):
            sx = maps((self.x)/self.z,0 ,1 ,0 ,width)
            sy = maps((self.y)/self.z,0 ,1 ,0 ,height)
            r = maps(self.z ,0 ,width ,6 ,0)
            pygame.draw.circle(surf ,('white'), (int(sx+width/2) ,int(sy+height/2)) ,r)
        
        def update(self):
            self.z -= 5
            if self.z < 1:
                self.x = random.randint(-width ,width)
                self.y = random.randint(-height ,height)  
                self.z = random.randint(1 ,width)

    def maps(num ,in_min ,in_max ,out_min ,out_max):
        return (num - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;

    stars = []
    for i in range(500):
        s = Star()
        stars.append(s)   
    
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
        surf.fill((0,0,0))
        for s in stars:
            s.update()
            s.draw(surf)
        pygame.display.flip()

draw_stars()   





