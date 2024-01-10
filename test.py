import pygame
pygame.init()

# On crée une fenetre de 900 sur 600 px
surf = pygame.display.set_mode((900,600))
run = True
font_path = "./Pokemon Hollow.ttf"

class Case:
    # X et Y sont les coordonnées pour nos carré
    def __init__(self, x ,y):
        self.x = x 
        self.y = y
    
    def draw_case(self):
        pygame.draw.rect(surf ,(0,0,0) ,(self.x ,self.y ,100 ,100) ,2)
    
    def close_menu(self):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (1,0,0):
                print ("gg")
    
    def get_pokemon(self ,link ,posx ,posy):
        pokemon = pygame.image.load(link)
        surf.blit(pokemon ,(posx ,posy))
    
    def draw_text(self):
        police = pygame.font.Font(font_path ,35)
        img_texte = police.render ("Choose Your Pokemon !",1,(0,0,0))
        surf.blit(img_texte,(245 ,270))
        

# Initialisation des case correspondant à chaque pokemon
poussifeu = Case (80 ,20)
galifeu = Case (380 ,20)
brasegali = Case(700 ,20)
gobou = Case (80 ,160)
flobio = Case (380 ,160)
laggron = Case(700 ,160)
miaouss = Case (80 ,320)
zigzaton = Case (380 ,320)
ronflex = Case(700 ,320)
osselait = Case (80 ,480)
sabelette = Case (380 ,480)
groudon = Case(700 ,480)
text = Case (350 ,300)



while run :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # Définir un fond blanc
    surf.fill((255,255,255))

    # Dessiner les cases

    poussifeu.draw_case()
    galifeu.draw_case()
    brasegali.draw_case()
    gobou.draw_case()
    flobio.draw_case()
    laggron.draw_case()
    miaouss.draw_case()
    zigzaton.draw_case()
    ronflex.draw_case()
    osselait.draw_case()
    sabelette.draw_case()
    groudon.draw_case()

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
    pygame.display.flip()
pygame.quit()