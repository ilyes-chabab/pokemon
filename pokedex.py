from pokemon import Pokemon
import pygame
import sys

class Pokedex:
    def __init__(self):
        self.pokedex=False

    
    def toutLesPokemon(self):
        self.Poussifeu=Pokemon("Poussifeu",  40,  1, "feu", 14, 0.80, "poussifeu.png")
        Galifeu=Pokemon("Galifeu",  40,  1, "feu", 14, 0.80, "galifeu.png")
        Brasegali=Pokemon("Brasegali",  40,  1, "feu", 14, 0.80, "brasegali.png") 
     
     
    #  "Gobou",  40,  1, "eau", 12, 0.90, "gobou.png"
    #  "Flobio",  40,  1, "eau", 12, 0.90, "flobio.png"
    #  "Laggron",  40,  1, "eau", 12, 0.90, "laggron.png"
    #  "Miaouss",  40,  1, "normal", 13, 0.85, "miaouss.png"
    #  "Zigzaton",  40,  1, "normal", 13, 0.85, "zigzaton.png"
    #  "Ronflex",  40,  1, "normal", 13, 0.85, "ronflex.png"
    #  "Osselait",  40,  1, "sol", 16, 0.70, "osselait.png"
    #  "Sabelette",  40,  1, "sol", 16, 0.70, "sabelette.png"
    #  "Groudon",  40,  1, "sol", 16, 0.70, "groudon.png"
    def highlight(self, text, position):
        my_font = pygame.font.Font(None, 50)
        highlighted_text = my_font.render(text, 1, (255, 255, 0))
        self.screen.blit(highlighted_text, position)
        pygame.display.update()
    def pokedex_loop(self):
        pygame.init()
        screen=pygame.display.set_mode((900,600))
        while self.pokedex:
            screen.fill((250,250,250))
            for event in pygame.event.get() :
                if event.type == pygame.QUIT:
                    sys.exit()
                self.highlight(self.Poussifeu.nom,(500,500))
            pygame.display.flip()
