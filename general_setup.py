import pygame, sys
'''---------------------------------SETUP-------------------------------'''
# General setup
pygame.init()
clock = pygame.time.Clock()

# Setting up the main window
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Game Title')

'''----------------------------------LOOP-------------------------------'''
while True:
    #Handling input (EVENTS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
            sys.exit()

    # Drawing

    # Updating the window 
    pygame.display.flip()
    clock.tick(60)