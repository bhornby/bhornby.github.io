# Import the pygame library and initialise the game engine
import pygame
from random import randint
pygame.init()
 
# Define some colors
BLACK = (0,0,0)
WHITE = (255,255,255)
GREY = (180,180,180)
GREEN = (0,240,0)
RED = (240,0,0)
clock = pygame.time.Clock()
# Open a new window
size = (1280,720)
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode(size)
pygame.display.set_caption("SI")

class PlayerBullet(pygame.sprite.Sprite):
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        # Pass in the color of the paddle, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([4, 7])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        

    def udpate(self):
        self.rect.y-=11


class Base(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        # Pass in the color of the paddle, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([10, 10])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x=x
        self.rect.y=y

    

class Player(pygame.sprite.Sprite):
    #This class represents a paddle. It derives from the "Sprite" class in Pygame.
    
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        # Pass in the color of the paddle, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        self.speed=5
         
        # Draw the paddle (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        
    def moveLeft(self, pixels):
        self.rect.x -= pixels
        #Check that you are not going too far (off the screen)
        if self.rect.x < 0:
          self.rect.x = 0
          
    def moveRight(self, pixels):
        self.rect.x += pixels
    #Check that you are not going too far (off the screen)
        if self.rect.x > 1230:
          self.rect.x = 1230
          
    



class Alien(pygame.sprite.Sprite):
    #This class represents a ball. It derives from the "Sprite" class in Pygame.
    
    def __init__(self, color, x, y):
        """ Constructor. Pass in the color of the block,
        and its x and y position. """
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([20, 20])
        self.image.fill(color)
        self.health = 1
        #self.width=100
        #self.height=100
 
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
 
    def reset_pos(self):
        """ Reset position to the top of the screen, at a random x location.
        Called by update() or the main program loop if there is a collision.
        """
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.randrange(0, screen_width)
 
    def update(self):
        if self.health <= 0:
            self.kill()
                        
            
        pygame.display.flip()
        clock.tick(60)
               

def gameloop():
    player = Player(GREEN, 30, 30)
    player.rect.x = 620
    player.rect.y = 650

    
    
#This will be a list that will contain all the sprites we intend to use in our game.
    block_list = pygame.sprite.Group()
    all_sprites_list = pygame.sprite.Group()

    count=2
    for i in range(100, 400, 50):
    
        for x in range(100, 1200, 100):
    # This represents a block
            if count%2==0:
            
                block = Alien(WHITE, x, i)
            else:
                x=x+50
                
                block = Alien(WHITE, x, i)
         
        # Set a random location for the block
       
     
        # Add the block to the list of objects
            block_list.add(block)
            all_sprites_list.add(block)
        count+=1

    count=2
    for i in range(500, 540, 5):
    
        for x in range(150, 250, 10):
    # This represents a block
            if count%2==0:
            
                base = Base(RED, x, i)
            else:
                
                
                base = Base(RED, x, i)
         
        # Set a random location for the block
       
     
        # Add the block to the list of objects
            block_list.add(base)
            all_sprites_list.add(base)
        count+=1
# The loop will carry on until the user exit the game (e.g. clicks the close button).
    carryOn = True
 
# The clock will be used to control how fast the screen updates

#Initialise player scores

# -------- Main Program Loop -----------
    while carryOn:
    # --- Main event loop
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
              carryOn = False # Flag that we are done so we exit this loop
            elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE: #Pressing the x Key will quit the game
                         carryOn=False
 
    #Moving the paddles when the user uses the arrow keys (player A) or "W/S" keys (player B) 
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            player.moveLeft(7)
        if keys[pygame.K_d]:
            player.moveRight(7)   
        if keys[pygame.K_SPACE]:
            bullet = PlayerBullet()
            bullet.rect.x = player.rect.x - 2
            bullet.rect.y = player.rect.y
            all_sprites_list.add(bullet)
            
            
    # --- Game logic should go here
        
        
 
  #Check if the ball is bouncing against any of the 4 walls:
        


        all_sprites_list.add(player)
                   
        
    #Detect collisions between the ball and the paddles
        all_sprites_list.update()
    # --- Drawing code should go here
    # First, clear the screen to black. 
        screen.fill(BLACK)
    
        
    
    #Now let's draw all the sprites in one go. (For now we only have 2 sprites!)
        all_sprites_list.draw(screen) 

        
    # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
     
    # --- Limit to 60 frames per second
        clock.tick(60)


 
#Once we have exited the main program loop we can stop the game engine:

pygame.quit()