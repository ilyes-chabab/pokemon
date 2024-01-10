import pygame 
import sys


def page_accueil():
    pygame.init()

    width,height = 900,600

    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption("Pokémon")
    #Logo "Pokémon"
    logo = pygame.image.load('logo/Pokemon_logo.png')
    image_size = (550, 150)
    #Mise à l'échelle de l'image.
    logo=pygame.transform.scale(logo, image_size)
    #Position de l'image par rapport au dimmension de la fenetre de jeu 
    logo_position = (175,0)
    #Photo des deux pokemon legendaire
    img_groudon=pygame.image.load('image_menu/Groudon.png')
    img_groudon=pygame.transform.scale(img_groudon, (250,175))
    groudon_position = (0,250)
    img_kyogre=pygame.image.load('image_menu/Kyogre.png')
    img_kyogre=pygame.transform.scale(img_kyogre, (250,175))
    kyogre_position = (650,250)
    
    #couleur de fond
    screen.fill((250,137,0))
    pygame.font.init()
    #initialisation de la musique
    pygame.mixer.init()
    #chargement musique de fond
    pygame.mixer.music.load('music-menu/Pokemon-menu-music.mp3')
    #Musique de fond
    pygame.mixer.music.play()

    while True:

        for event in pygame.event.get() :
            
            #Option de jeu
            My_font=pygame.font.Font(None, 50)        
            text = My_font.render("Jouer",1,(255,255,255))
            screen.blit(text,(400,200))
            text = My_font.render("Voir le Pokédex",1,(255,255,255))
            screen.blit(text,(325,300))
            text = My_font.render("Plus de Pokémon",1,(255,255,255))
            screen.blit(text,(310,400))
            
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
            elif event.type== pygame.MOUSEMOTION:
                (x,y)=pygame.mouse.get_pos()
                if 400<x<500 and 200<y<230:
                    text = My_font.render("Jouer",1,(255,255,0))
                    screen.blit(text,(400,200))
                elif 325<x<580 and 300<y<330:
                    text = My_font.render("Voir le Pokédex",1,(255,255,0))
                    screen.blit(text,(325,300))
                elif 310<x<600 and 400<y<430:
                    text = My_font.render("Plus de Pokémon",1,(255,255,0))
                    screen.blit(text,(310,400))
                    
        
        screen.blit(logo,logo_position)
        screen.blit(img_groudon,groudon_position)
        screen.blit(img_kyogre,kyogre_position)

        
        pygame.display.flip()
page_accueil()
           

