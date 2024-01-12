import pygame
import sys

class PageAccueil:
    
    def __init__(self):
        pygame.init()
        
        self.width, self.height = 900, 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Pokémon")

        # Logo "Pokémon"
        self.logo = pygame.image.load('logo/Pokemon_logo.png')
        # Mise à l'échelle de l'image.
        image_size = (550, 150)
        self.logo = pygame.transform.scale(self.logo, image_size)
        # Position de l'image par rapport au dimension de la fenêtre de jeu
        self.logo_position = (175, 0)

        # Photo des deux Pokémon légendaires
        self.img_groudon = pygame.image.load('image_menu/Groudon.png')
        self.img_groudon = pygame.transform.scale(self.img_groudon, (250, 175))
        self.groudon_position = (0, 250)

        self.img_kyogre = pygame.image.load('image_menu/Kyogre.png')
        self.img_kyogre = pygame.transform.scale(self.img_kyogre, (250, 175))
        self.kyogre_position = (650, 250)

        # Couleur de fond
        self.screen.fill((0, 0, 0))
        pygame.font.init()
        # Initialisation de la musique
        pygame.mixer.init()
        # Chargement musique de fond
        pygame.mixer.music.load('music-menu/Pokemon-menu-music.mp3')
        # Musique de fond
        pygame.mixer.music.play()

        self.Menu_principal()    

    def Menu_principal(self):
        while True:
            # Option de jeu exemple:Jouer,plus de pokemon ...
            self.Option_de_jeu()
            # Image logo + 2 pokémons
            self.screen.blit(self.logo, self.logo_position)
            self.screen.blit(self.img_groudon, self.groudon_position)
            self.screen.blit(self.img_kyogre, self.kyogre_position)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.Hyperlien_jeu()
                elif event.type == pygame.MOUSEMOTION:
                    self.hover()
                pygame.display.update()
            

    def Hyperlien_jeu(self):
        (x, y) = pygame.mouse.get_pos()
        if 400 < x < 500 and 200 < y < 230:
            print('Jouer')
        elif 325 < x < 580 and 300 < y < 330:
            print('Voir le Pokédex')
        elif 310 < x < 600 and 400 < y < 430:
            print('Plus de Pokémon')

    def hover(self):
        (x, y) = pygame.mouse.get_pos()
        if 400 < x < 500 and 200 < y < 230:
            self.highlight("Jouer", (400, 200))
        elif 325 < x < 580 and 300 < y < 330:
            self.highlight("Voir le Pokédex", (325, 300))
        elif 310 < x < 600 and 400 < y < 430:
            self.highlight("Plus de Pokémon", (310, 400))

    def highlight(self, text, position):
        my_font = pygame.font.Font(None, 50)
        highlight_text = my_font.render(text, 1, (255, 255, 0))
        self.screen.blit(highlight_text, position)
        pygame.display.update()

    def Option_de_jeu(self):
        my_font = pygame.font.Font(None, 50)
        # Option de jeu
        text = my_font.render("Jouer", 1, (255, 255, 255))
        self.screen.blit(text, (400, 200))
        text = my_font.render("Voir le Pokédex", 1, (255, 255, 255))
        self.screen.blit(text, (325, 300))
        text = my_font.render("Plus de Pokémon", 1, (255, 255, 255))
        self.screen.blit(text, (310, 400))
    

# Création de l'instance de Classe 
page_accueil = PageAccueil()

