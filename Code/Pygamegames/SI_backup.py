import pygame
pygame.init()

#defining colors
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)

#set display
size  = (1280,720)
screen_width = 1280
screen_heigt = 720
screen = pygame.display.set_mode(size)
pygame.display.set_caption("test")

clock = pygame.time.Clock()
#loop until user clicks close button
done = False

# starting possition of object
x_offset = 0
y_offset = 0

ellipse_x = 80
ellipse_y = 50

#speed and direction change
ellipse_change_x = 5
ellipse_change_y = 5

#main program loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    #game logic

    #drawing code
    screen.fill(BLACK)
    
    pygame.draw.ellipse(screen, GREEN, [ellipse_x, elipse_y, 40, 30])
    ellipse_x += 1

    

    while x_offset < 1120:
        #draw the echlips body
        pygame.draw.ellipse(screen, GREEN, [80 + x_offset, 50, 40,30])
        
        x_offset = x_offset + 80
        y_offset = y_offset 
        
        
    
    
        
    
        
    

    #refreshes the screen
    pygame.display.flip()
    
    #limits to 60 fps
    clock.tick(60)

pygame.quit()











