import pygame
import time
from pygame import mixer
pygame.init()

# On crée une fenetre de 900 sur 600 px
surf = pygame.display.set_mode((900,600))
timer = pygame.time.Clock()
run = True
mixer.music.load('battlemusic.mp3')
noir_fond = pygame.image.load("image_arene/fond_noir.jpg")
img_fond = pygame.image.load("image_arene/fondarenecombat.jpg")
fond_size = (900,600)
fond = pygame.transform.scale(img_fond ,fond_size)
fond_noir = pygame.transform.scale(noir_fond ,fond_size)
font_path = "font_interface/Pokemon Solid.ttf"

import pygame
import time
pygame.init()

 
class Case:
    
    def __init__(self):
        pass
    
    # X et Y sont les coordonnées pour nos carré
    def draw_case(self ,x ,y):
        pygame.draw.rect(surf ,(255,255,255) ,(x ,y ,100 ,100) ,2)
    
    def close_menu(self):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (1,0,0):
                print ("gg")
    
    def get_pokemon(self ,link ,posx ,posy):
        pokemon = pygame.image.load(link)
        surf.blit(pokemon ,(posx ,posy))
    
    def draw_text(self):
        police = pygame.font.Font(font_path ,35)
        img_texte = police.render ("Choose Your Pokemon !",1,(255,255,255))
        surf.blit(img_texte,(245 ,270))
        img_pokeball = pygame.image.load("image_arene/pokeball.png")
        poke_size = (40,40)
        image = pygame.transform.scale(img_pokeball ,poke_size)
        surf.blit(image,(180,270))
        surf.blit(image,(670,270))
    
    def get_pos(self ,a ,z ,e ,r ,dos ,c ,v ,face ,j ,k):
        face_pokemon = pygame.image.load(face)
        dos_pokemon = pygame.image.load(dos)
        dos_size = (280,280)
        resultat = pygame.transform.scale(dos_pokemon ,dos_size)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (1,0,0) :
                x , y = pygame.mouse.get_pos()
                if x >= (a) and x <= (z) and y >= (e) and y <= (r):
                    surf.blit(fond_noir ,(0,0))
                    pygame.draw.rect(surf ,(255,255,255) ,(a ,e ,100 ,100) ,2)
                    surf.blit(face_pokemon ,(j ,k))
                    mixer.music.play(-1)
                    pygame.display.update()
                    time.sleep(3)
                    surf.blit(fond ,(0,0))
                    surf.blit(resultat, (c,v))
                    
                    
        
        

# Initialisation des case correspondant à chaque pokemon
poussifeu = Case ()
galifeu = Case ()
brasegali = Case()
gobou = Case ()
flobio = Case ()
laggron = Case()
miaouss = Case ()
zigzaton = Case ()
ronflex = Case()
osselait = Case ()
sabelette = Case ()
groudon = Case()
text = Case ()

def choose_pokemon():

    # Remplir le fond en noir
    surf.fill((0,0,0))

    # Dessiner les cases

    poussifeu.draw_case(80 ,20)
    galifeu.draw_case(380 ,20)
    brasegali.draw_case(700 ,20)
    gobou.draw_case(80 ,160)
    flobio.draw_case(380 ,160)
    laggron.draw_case(700 ,160)
    miaouss.draw_case(80 ,320)
    zigzaton.draw_case(380 ,320)
    ronflex.draw_case(700 ,320)
    osselait.draw_case(80 ,480)
    sabelette.draw_case(380 ,480)
    groudon.draw_case(700 ,480)

    # Afficher les images des pokemons dans les cases

    poussifeu.get_pokemon("img_pokemon/poussifeu.png" ,98 ,40)
    galifeu.get_pokemon("img_pokemon/galifeu.png" ,398 ,40)
    brasegali.get_pokemon("img_pokemon/brasegali.png",715 ,40)
    gobou.get_pokemon("img_pokemon/gobou.png",98 ,180)
    flobio.get_pokemon("img_pokemon/flobio.png",398 ,180)
    laggron.get_pokemon("img_pokemon/laggron.png",720 ,180)
    miaouss.get_pokemon("img_pokemon/miaouss.png",98 ,340)
    zigzaton.get_pokemon("img_pokemon/zigzaton.png",398 ,340)
    ronflex.get_pokemon("img_pokemon/ronflex.png",720 ,340)
    osselait.get_pokemon("img_pokemon/osselait.png" ,98 ,500)
    sabelette.get_pokemon("img_pokemon/sabelette.png" ,398 ,500)
    groudon.get_pokemon("img_pokemon/groudon.png" ,720 ,500)

    # Afficher le texte
    text.draw_text()

    

choose_pokemon()

while run :
    timer.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
   
        # Cliquer dans la case
        poussifeu.get_pos(80 ,180 ,20 ,120 ,"dos_pokemon/poussifeudos.png" ,50 ,350 ,"img_pokemon/poussifeu.png" ,98 ,40)
        galifeu.get_pos(380 ,480 ,20 ,120 ,"dos_pokemon/galifeudos.png" ,50 ,320 ,"img_pokemon/galifeu.png" ,398 ,40)
        brasegali.get_pos(700 ,800 ,20 ,120 ,"dos_pokemon/brasegalidos.png" ,50 ,320 ,"img_pokemon/brasegali.png" ,715 ,40)
        gobou.get_pos(80 ,180 ,160 ,260 ,"dos_pokemon/goboudos.png" ,50 ,340)
        flobio.get_pos(380 ,480 ,160 ,260 ,"dos_pokemon/flobiodos.png" ,50 ,340)
        laggron.get_pos(700 ,800 ,160 ,260 ,"dos_pokemon/laggrondos.png" ,50 ,340)
        miaouss.get_pos(80 ,180 ,320 ,420 ,"dos_pokemon/miaoussdos.png" ,50 ,375)
        zigzaton.get_pos(380 ,480 ,320 ,420 ,"dos_pokemon/zigzatondos.png" ,50 ,370)
        ronflex.get_pos(700 ,800 ,320 ,420 ,"dos_pokemon/ronflexdos.png" ,50 ,370)
        osselait.get_pos(80 ,180 ,480 ,580 ,"dos_pokemon/osselaitdos.png" ,50 ,365)
        sabelette.get_pos(380 ,480 ,480 ,580 ,"dos_pokemon/sabelettedos.png" ,50 ,378)
        groudon.get_pos(700 ,800 ,480 ,580 ,"dos_pokemon/groudondos.png" ,50 ,355)
        pygame.display.flip()

        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_SPACE :
                choose_pokemon()
pygame.quit()