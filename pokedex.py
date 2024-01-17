from pokemon import Pokemon
import pygame
import sys

class Pokedex:
    def __init__(self):
        pygame.init()
        self.pokedex=True
        #initialisation des pokemon
        self.Poussifeu=Pokemon("Poussifeu",  40,  1, "feu", 14, 0.80, "img_pokemon/poussifeu.png")
        self.Galifeu=Pokemon("Galifeu",  40,  1, "feu", 14, 0.80, "img_pokemon/galifeu.png")
        self.Brasegali=Pokemon("Brasegali",  40,  1, "feu", 14, 0.80, "img_pokemon/brasegali.png")   
        self.Gobou=Pokemon("Gobou",  40,  1, "eau", 12, 0.90, "img_pokemon/gobou.png")   
        self.Flobio=Pokemon("Flobio",  40,  1, "eau", 12, 0.90, "img_pokemon/flobio.png")
        self.Laggron=Pokemon("Laggron",  40,  1, "eau", 12, 0.90, "img_pokemon/laggron.png")
        self.Miaouss=Pokemon("Miaouss",  40,  1, "normal", 13, 0.85, "img_pokemon/miaouss.png")
        self.Zigzaton=Pokemon("Zigzaton",  40,  1, "normal", 13, 0.85, "img_pokemon/zigzaton.png")
        self.Ronflex=Pokemon("Ronflex",  40,  1, "normal", 13, 0.85, "img_pokemon/ronflex.png")
        self.Osselait=Pokemon("Osselait",  40,  1, "sol", 16, 0.70, "img_pokemon/osselait.png")
        self.Sabelette=Pokemon("Sabelette",  40,  1, "sol", 16, 0.70, "img_pokemon/sabelette.png")
        self.Groudon=Pokemon("Groudon",  40,  1, "sol", 16, 0.70, "img_pokemon/groudon.png")
        self.screen=pygame.display.set_mode((1200,600)) 
        #creation des images
        image_Poussifeu = pygame.image.load(self.Poussifeu.image)
        self.image_Poussifeu = pygame.transform.scale(image_Poussifeu,(80,60))
        image_Galifeu = pygame.image.load(self.Galifeu.image)
        self.image_Galifeu = pygame.transform.scale(image_Galifeu,(80,60))
        image_Brasegali = pygame.image.load(self.Brasegali.image)
        self.image_Brasegali = pygame.transform.scale(image_Brasegali,(80,60))
        image_Gobou = pygame.image.load(self.Gobou.image)
        self.image_Gobou = pygame.transform.scale(image_Gobou,(80,60))
        image_Flobio = pygame.image.load(self.Flobio.image)
        self.image_Flobio = pygame.transform.scale(image_Flobio,(80,60))
        image_Laggron = pygame.image.load(self.Laggron.image)
        self.image_Laggron = pygame.transform.scale(image_Laggron,(80,60))
        image_Miaouss = pygame.image.load(self.Miaouss.image)
        self.image_Miaouss = pygame.transform.scale(image_Miaouss,(80,60))
        image_Zigzaton = pygame.image.load(self.Zigzaton.image)
        self.image_Zigzaton = pygame.transform.scale(image_Zigzaton,(80,60))
        image_Ronflex = pygame.image.load(self.Ronflex.image)
        self.image_Ronflex = pygame.transform.scale(image_Ronflex,(80,60))
        image_Osselait = pygame.image.load(self.Osselait.image)
        self.image_Osselait = pygame.transform.scale(image_Osselait,(80,60))
        image_Sabelette = pygame.image.load(self.Sabelette.image)
        self.image_Sabelette = pygame.transform.scale(image_Sabelette,(80,60))
        image_Groudon = pygame.image.load(self.Groudon.image)
        self.image_Groudon = pygame.transform.scale(image_Groudon,(80,60))

        self.pokedex_Poussifeu=False
        self.pokedex_Galifeu=False
        self.pokedex_Brasegali=False
        self.pokedex_Gobou=False
        self.pokedex_Flobio=False
        self.pokedex_Laggron=False
        self.pokedex_Miaouss=False
        self.pokedex_Zigzaton=False
        self.pokedex_Ronflex=False
        self.pokedex_Osselait=False
        self.pokedex_Sabelette=False
        self.pokedex_Groudon=False

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
            if self.pokedex_Poussifeu:
                self.highlight(f"Nom : {self.Poussifeu.nom}, Vie : {self.Poussifeu.vie}, Niveau : {self.Poussifeu.niveau}",(100,0))
                self.highlight(f"Type : {self.Poussifeu.type},  Puissance : {self.Poussifeu.puissance}, Defense : {self.Poussifeu.defense}",(100,20))
                self.screen.blit(self.image_Poussifeu,(0,0))
            if self.pokedex_Galifeu:
                self.highlight(f"Nom : {self.Galifeu.nom}, Vie : {self.Galifeu.vie}, Niveau : {self.Galifeu.niveau}",(100,60))
                self.highlight(f"Type : {self.Galifeu.type},  Puissance : {self.Galifeu.puissance}, Defense : {self.Galifeu.defense}",(100,80))
                self.screen.blit(self.image_Galifeu,(0,50))
            if self.pokedex_Brasegali:
                self.highlight(f"Nom : {self.Brasegali.nom}, Vie : {self.Brasegali.vie}, Niveau : {self.Brasegali.niveau}",(100,120))
                self.highlight(f"Type : {self.Brasegali.type},  Puissance : {self.Brasegali.puissance}, Defense : {self.Brasegali.defense}",(100,140))
                self.screen.blit(self.image_Brasegali,(0,110))
            if self.pokedex_Gobou:
                self.highlight(f"Nom : {self.Gobou.nom}, Vie : {self.Gobou.vie}, Niveau : {self.Gobou.niveau}",(100,180))
                self.highlight(f"Type : {self.Gobou.type},  Puissance : {self.Gobou.puissance}, Defense : {self.Gobou.defense}",(100,200))
                self.screen.blit(self.image_Gobou,(0,165))
            if self.pokedex_Flobio:
                self.highlight(f"Nom : {self.Flobio.nom}, Vie : {self.Flobio.vie}, Niveau : {self.Flobio.niveau}",(100,240))
                self.highlight(f"Type : {self.Flobio.type},  Puissance : {self.Flobio.puissance}, Defense : {self.Flobio.defense}",(100,260))
                self.screen.blit(self.image_Flobio,(0,210))
            if self.pokedex_Laggron:
                self.highlight(f"Nom : {self.Laggron.nom}, Vie : {self.Laggron.vie}, Niveau : {self.Laggron.niveau}",(100,300))
                self.highlight(f"Type : {self.Laggron.type},  Puissance : {self.Laggron.puissance}, Defense : {self.Laggron.defense}",(100,320))
                self.screen.blit(self.image_Laggron,(0,270)) 
            if self.pokedex_Miaouss:
                self.highlight(f"Nom : {self.Miaouss.nom}, Vie : {self.Miaouss.vie}, Niveau : {self.Miaouss.niveau}",(650,0))
                self.highlight(f"Type : {self.Miaouss.type},  Puissance : {self.Miaouss.puissance}, Defense : {self.Miaouss.defense}",(650,20))
                self.screen.blit(self.image_Miaouss,(550,0))
            if self.pokedex_Zigzaton:
                self.highlight(f"Nom : {self.Zigzaton.nom}, Vie : {self.Zigzaton.vie}, Niveau : {self.Zigzaton.niveau}",(650,60))
                self.highlight(f"Type : {self.Zigzaton.type},  Puissance : {self.Zigzaton.puissance}, Defense : {self.Zigzaton.defense}",(650,80))
                self.screen.blit(self.image_Zigzaton,(550,50))
            if self.pokedex_Ronflex:
                self.highlight(f"Nom : {self.Ronflex.nom}, Vie : {self.Ronflex.vie}, Niveau : {self.Ronflex.niveau}",(650,120))
                self.highlight(f"Type : {self.Ronflex.type},  Puissance : {self.Ronflex.puissance}, Defense : {self.Ronflex.defense}",(650,140))
                self.screen.blit(self.image_Ronflex,(550,110))
            if self.pokedex_Osselait:
                self.highlight(f"Nom : {self.Osselait.nom}, Vie : {self.Osselait.vie}, Niveau : {self.Osselait.niveau}",(650,180))
                self.highlight(f"Type : {self.Osselait.type},  Puissance : {self.Osselait.puissance}, Defense : {self.Osselait.defense}",(650,200))
                self.screen.blit(self.image_Osselait,(550,165))
            if self.pokedex_Sabelette:
                self.highlight(f"Nom : {self.Sabelette.nom}, Vie : {self.Sabelette.vie}, Niveau : {self.Sabelette.niveau}",(650,240))
                self.highlight(f"Type : {self.Sabelette.type},  Puissance : {self.Sabelette.puissance}, Defense : {self.Sabelette.defense}",(650,260))
                self.screen.blit(self.image_Sabelette,(550,210))
            if self.pokedex_Groudon:
                self.highlight(f"Nom : {self.Groudon.nom}, Vie : {self.Groudon.vie}, Niveau : {self.Groudon.niveau}",(650,300))
                self.highlight(f"Type : {self.Groudon.type},  Puissance : {self.Groudon.puissance}, Defense : {self.Groudon.defense}",(650,320))
                self.screen.blit(self.image_Groudon,(550,270))          

            pygame.display.flip()
run=Pokedex()
run.pokedex_loop()
