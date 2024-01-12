import pygame
import time
pygame.init()

class ParticleStar:
    def __init__(self):
        self.particles = []
    
    def emit(self):
        if self.particles:
            self.delete_particles()
            for particle in self.particles:
                particle[0][1] += particle[2][0]
                particle[0][0] += particle[2][1]
                particle[1]-= 0.2
                pygame.draw.circle(surf,pygame.Color('White'),particle[0], int(particle[1]))


