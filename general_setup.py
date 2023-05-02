import pygame, sys

#global variables
screen_width = 1280
screen_height = 960

'''---------------------------------SPRITES/CLASSES---------------------'''

'''---------------------------------SETUP-------------------------------'''
# General setup
pygame.init()
clock = pygame.time.Clock()

# Setting up the main window
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Game Title')

# Define Custom Events

# Instantiate objects and groups


'''----------------------------------LOOP-------------------------------'''
while True:
    #Handling input (EVENTS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Drawing
    screen.fill('black') #replace with image or whatever you use up top

    # Updating the window
    pygame.display.flip()
    clock.tick(60)
