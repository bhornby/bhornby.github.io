"""
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/
 
Explanation video: http://youtu.be/qbEEcQXw8aw
"""
 
import pygame
import random
from random import randint
pygame.init()
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

clock = pygame.time.Clock

# open the window
size = (1280,720)
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Space Invaders")


 
class Player(pygame.sprite.Sprite):
     # this class is for the player
     
    def __init__(self, color, x, y):
        """ Constructor. Pass in the color of the block,
        and its x and y position. """
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk. 20 20 is just the width and the height.
        self.image = pygame.Surface([4, 10])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        
        def update (self):
            
            self.rect.y = 10



 
    def reset_pos(self):
        """ Reset position to the top of the screen, at a random x location.
        Called by update() or the main program loop if there is a collision.
        """
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.randrange(0, screen_width)
 
#     def update(self):
#         """ Called each frame. """
#  
#         # Move block down one pixel
#         self.rect.y + = 1
#  
#         # If block is too far down, reset to top of screen.
#         if self.rect.y > 600:
#             self.rect.y=100
 
 
class Player(pygame.sprite.sprite):
   #this class is the player
    
    def __init__(self):
        # makes player by calling parent class
        super().__init__()
        
        self.image = pygame.draw([20, 20])
        self.image.fill = (GREEN)
        
        self.rect = self.image.get_rect:() 
    
 
# Initialize Pygame
pygame.init()
 
# Set the height and width of the screen
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode([screen_width, screen_height])
 
# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
block_list = pygame.sprite.Group()
 
# This is a list of every sprite. All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()

count=2
for i in range(100, 400, 50):
    
    for x in range(100, 900, 100):
    # This represents a block
        if count%2==0:
            
            block = Block(GREEN, x, i)
        else:
            x=x+50
            print(x)
            block = Block(GREEN, x, i)
         
        # Set a random location for the block
       
     
        # Add the block to the list of objects
        block_list.add(block)
        all_sprites_list.add(block)
    count+=1
 
# Create a red player block
#player = Player(RED, 20, 15)
#all_sprites_list.add(player)
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
score = 0
 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # Clear the screen
    screen.fill(BLACK)
 
    # Calls update() method on every sprite in the list
    all_sprites_list.update()
 
    # See if the player block has collided with anything.
    #blocks_hit_list = pygame.sprite.spritecollide(player, block_list, False)
 
    # Check the list of collisions.
    
 
    # Draw all the spites
    all_sprites_list.draw(screen)
 
    # Limit to 20 frames per second
    clock.tick(20)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
pygame.quit()