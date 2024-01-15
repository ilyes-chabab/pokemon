import pygame
import time
pygame.init()

<<<<<<< HEAD
# On crée une fenetre de 900 sur 600 px
surf = pygame.display.set_mode((900,600))
timer = pygame.time.Clock()
run = True
run2 = True
verif1 = 0
verif2 = 0
fond = pygame.image.load("image_arene/fondarenecombat.jpg")
font_path = "font_interface/Pokemon Solid.ttf"

class Case:
    
    def __init__(self):
        pass

    
    # X et Y sont les coordonnées pour nos carré
    def draw_case(self ,x ,y):
        pygame.draw.rect(surf ,(255,255,255) ,(x ,y ,100 ,100) ,2)
    
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

    
    def get_pos(self ,a ,z ,e ,r):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == (1,0,0) :
                    x , y = pygame.mouse.get_pos()
                    if x >(a) and x < (z) and y > (e) and y < (r):
                        print ("gg")
                        
                    

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


    
while run :
    timer.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

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

        # Afficher le texte et la pokéball
        text.draw_text()

        
        # Cliquer dans la case
        
        poussifeu.get_pos(80 ,180 ,20 ,120)
        galifeu.get_pos(380 ,480 ,20 ,120)
        brasegali.get_pos(700 ,800 ,20 ,120)
        
        pygame.display.flip()
pygame.quit()


=======
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
>>>>>>> origin/interface


