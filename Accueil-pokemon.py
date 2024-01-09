import pygame 
import sys


def page_accueil():
    pygame.init()

    width,height = 900,600

    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption("Pokémon")
    #fond d'ecran
    logo = pygame.image.load('logo/Pokemon_logo.png')
    DEFAULT_IMAGE_SIZE = (550, 150)
    logo=pygame.transform.scale(logo, DEFAULT_IMAGE_SIZE)
    logo_position = (175,0)
    
    #couleur de fond
    screen.fill((0,0,0))
    pygame.font.init()
    pygame.mixer.init()
    pygame.mixer.music.load('music/Pokemon-menu-music.ogg')
    pygame.mixer.music.play()

    while True:

        for event in pygame.event.get() :
            
            
            
            
            # my_font=pygame.font.Font(None, 100)        
            #titre
            # text = my_font.render("Pokémon",1,(0,0,0))
            # screen.blit(text,(300,0))
            #Option de jeu
            My_font=pygame.font.Font(None, 50)        
            text = My_font.render("Jouer",1,(255,255,255))
            screen.blit(text,(400,200))
            text = My_font.render("Voir le Pokedex",1,(255,255,255))
            screen.blit(text,(325,300))
            text = My_font.render("Plus de pokemon",1,(255,255,255))
            screen.blit(text,(310,400))
            
            
            # pygame.mixer.music.play(-1)
            if event.type==pygame.QUIT:
                sys.exit()
            
            elif event.type== pygame.MOUSEBUTTONDOWN:
                (x,y)=pygame.mouse.get_pos()               
                if 400<x<500 and 200<y<230:
                    # importation de la fonction de jeu pur.
                    # jeu.partie_simple()
                    print('ok')
                    
                elif 325<x<580 and 300<y<330:
                    # importation de la fonction de jeu pur.
                    # jeu.partie_simple()
                    print('ok')
                elif 310<x<600 and 400<y<430:
                    # importation de la fonction de jeu pur.
                    # jeu.partie_simple()
                    print('ok')
        screen.blit(logo,logo_position)
        
        pygame.display.flip()
page_accueil()
           

