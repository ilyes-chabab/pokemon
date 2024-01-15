from pokemon import Pokemon
import pygame
import sys

class Pokedex:
    def __init__(self):
        pygame.init()
        self.pokedex=True
        
        self.Poussifeu=Pokemon("Poussifeu",  40,  1, "feu", 14, 0.80, "poussifeu.png")
        self.Galifeu=Pokemon("Galifeu",  40,  1, "feu", 14, 0.80, "galifeu.png")
        self.Brasegali=Pokemon("Brasegali",  40,  1, "feu", 14, 0.80, "brasegali.png")   
        self.Gobou=Pokemon("Gobou",  40,  1, "eau", 12, 0.90, "gobou.png")   
        self.Flobio=Pokemon("Flobio",  40,  1, "eau", 12, 0.90, "flobio.png")
        self.Laggron=Pokemon("Laggron",  40,  1, "eau", 12, 0.90, "laggron.png")
        self.Miaouss=Pokemon("Miaouss",  40,  1, "normal", 13, 0.85, "miaouss.png")
        self.Zigzaton=Pokemon("Zigzaton",  40,  1, "normal", 13, 0.85, "zigzaton.png")
        self.Ronflex=Pokemon("Ronflex",  40,  1, "normal", 13, 0.85, "ronflex.png")
        self.Osselait=Pokemon("Osselait",  40,  1, "sol", 16, 0.70, "osselait.png")
        self.Sabelette=Pokemon("Sabelette",  40,  1, "sol", 16, 0.70, "sabelette.png")
        self.Groudon=Pokemon("Groudon",  40,  1, "sol", 16, 0.70, "groudon.png")
        self.screen=pygame.display.set_mode((900,600)) 
     
     
     
        self.pokedex_loop()
    def highlight(self, text, position):
        my_font = pygame.font.Font(None, 30)
        highlighted_text = my_font.render(text, 1, (0,0,0))
        self.screen.blit(highlighted_text, position)
    def pokedex_loop(self):
        
        while True:
            self.screen.fill((250,250,250))
            for event in pygame.event.get() :
                if event.type == pygame.QUIT:
                    sys.exit()
            self.highlight(f"Nom : {self.Poussifeu.nom}, Vie : {self.Poussifeu.vie}, Niveau : {self.Poussifeu.niveau}",(100,0))
            self.highlight(f"Type : {self.Poussifeu.type},  Puissance : {self.Poussifeu.puissance}, Defense : {self.Poussifeu.defense}",(100,20))
            self.highlight(f"Nom : {self.Poussifeu.nom}, Vie : {self.Poussifeu.vie}, Niveau : {self.Poussifeu.niveau}",(100,70))
            self.highlight(f"Type : {self.Poussifeu.type},  Puissance : {self.Poussifeu.puissance}, Defense : {self.Poussifeu.defense}",(100,90))
            pygame.display.flip()
run=Pokedex()
run.pokedex_loop()
