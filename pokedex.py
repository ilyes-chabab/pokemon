from pokemon import Pokemon
import pygame
import sys

class Pokedex:

    pygame.init()
    screen=pygame.display.set_mode((900,600))


    while True:
        screen.fill((250,250,250))
        for event in pygame.event.get() :
             if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.flip()
