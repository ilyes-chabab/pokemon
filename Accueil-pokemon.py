
import pygame 
import sys


def page_accueil():
    pygame.init()

    width,height = 900,600

    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption("Pokémon")

    #couleur de fond
    screen.fill((255,255,255))
    pygame.font.init()
    
    while True:

        for event in pygame.event.get() :
            pygame.display.update() 
            my_font=pygame.font.Font(None, 100)        
            #titre
            text = my_font.render("Pokémon",1,(0,0,0))
            screen.blit(text,(300,0))
            #Option de jeu
            My_font=pygame.font.Font(None, 50)        
            text = My_font.render("Jouer",1,(0,0,0))
            screen.blit(text,(400,200))
            text = My_font.render("Voir le Pokedex",1,(0,0,0))
            screen.blit(text,(325,300))
            text = My_font.render("Plus de pokemon",1,(0,0,0))
            screen.blit(text,(310,400))
            (x,y)=pygame.mouse.get_pos()
            print(x,y)
            if event.type==pygame.QUIT:
                sys.exit()
            
            elif event.type== pygame.MOUSEBUTTONDOWN:
                x,y=pygame.mouse.get_pos()
                if 400<x<500 and 200<y<230:
                    #importation de la fonction de jeu pur.
                    # jeu.partie_simple()
                    print('ok')
                    
                elif 325<x<580 and 300<y<330:
                    #importation de la fonction de jeu pur.
                    # jeu.partie_simple()
                    print('ok')
                elif 310<x<600 and 400<y<430:
                    #importation de la fonction de jeu pur.
                    # jeu.partie_simple()
                    print('ok')

page_accueil()     
           

