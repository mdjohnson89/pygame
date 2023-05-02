import pygame, sys
'''---------------------------------SPRITES/CLASSES---------------------'''
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/fancy-paddle-blue.png')
        self.rect = self.image.getrect()
        self.speed = 7
        self.rect.center = (0, 480)


    def update():
        pass

class Opponent(Player):
    def __init__(self):
        super().__init__()
        self.rect.center = (480, 0)

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load()
        self.rect = self.image.getrect()

    def update():
        pass

'''---------------------------------SETUP-------------------------------'''
# General setup
pygame.init()
clock = pygame.time.Clock()

# Setting up the main window
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Game Title')

# Sprite Groups
paddle_group = pygame.Sprite.group()
opponent_group = pygame.Sprite.group()
ball_group = pygame.Sprite.group()

# Player
user = Player()
# Balls
ball = Ball()


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
