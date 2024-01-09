import pygame

surf = pygame.display.set_mode((900,600))
run = True
fond = pygame.image.load("fondarenecombat.jpg")
arcko = pygame.image.load("arcko2.gif")
arcko_size = (150,250)
image = pygame.transform.scale(arcko ,arcko_size)


while run :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    surf.blit(fond,(0,0))
    surf.blit(image,(50,400))
    pygame.display.flip()
pygame.quit()