import pygame

# On crée une fenetre de 900 sur 600 px
surf = pygame.display.set_mode((900,600))
run = True

class Case:
    # X et Y sont les coordonnées pour nos carré
    def __init__(self, x ,y):
        self.x = x 
        self.y = y
    
    def draw_case(self):
        pygame.draw.rect(surf ,(255,255,255) ,(self.x ,self.y ,200 ,200) ,2)

groudon = Case (50 ,50)







while run :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    surf.fill((0,0,0))
    poussifeu.draw_case()
    pygame.display.flip()
pygame.quit()