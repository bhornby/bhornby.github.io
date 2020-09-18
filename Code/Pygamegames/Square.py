import pygame
pygame.init()

Black = (0,0,0)
White = (255,255,255)
Red = (255,0,0)
Blue = (0,0,255)
Green = (0,255,0)

size = (700,500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Ben test")

done = False

clock = pygame.time.Clock()

while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(White)
    
    for x in range (0 ,100, 20):
        pygame.draw.line(screen, Blue, [0, 0], [100, 100], 5)

    pygame.display.flip()

    clock.tick(60)
        
pygame.quit()


