import pygame, sys, random

'''---------------------------------SPRITES/CLASSES-------------------------------'''
class Spaceship(pygame.sprite.Sprite):
    def __init__(self, picture_path):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(picture_path), (75, 75))
        self.rect = self.image.get_rect()
        self.damage = 0
    
    def update (self):
        self.rect.center = pygame.mouse.get_pos()
    
    def get_pos(self):
        return self.rect.center

class Asteroid(pygame.sprite.Sprite):
    '''Asteroid sprite -- essentially just moves down the screen. '''
    def __init__(self, picture_path, pos_x):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(picture_path), (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, 0]

    def update (self):
        self.rect.y += 5

class Laser(pygame.sprite.Sprite):
    def __init__(self, ship):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('Assets/laserBullet.png'), (75, 75))
        self.rect = self.image.get_rect()
        self.rect.center = ship.get_pos()
    
    def update(self):
        self.rect.y -= 5
        

'''---------------------------------SETUP-------------------------------'''
# General setup
pygame.init()
clock = pygame.time.Clock()

# Custom Events
MAX_DAMAGE = pygame.USEREVENT + 1
DESTROID = pygame.USEREVENT + 2

# Setting up the main window
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 960
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Game Title')
background = pygame.Color('black')

#Spaceship
spaceship = Spaceship('Assets/spaceship_red.png')
spaceship_group = pygame.sprite.Group()
spaceship_group.add(spaceship)

#Asteroids
asteroid = Asteroid('Assets/Asteroid_05.GIF', random.randrange(0, SCREEN_WIDTH))
asteroid_group = pygame.sprite.Group()
asteroid_group.add(asteroid)

# Lasers
laser = Laser(spaceship)
laser_group = pygame.sprite.Group()
laser_group.add(laser)

def check_laser(laser, asteroid):
    ''' Checks for laser / asteroid collisions '''
    for l in laser:
        for a in asteroid:
            if pygame.sprite.collide_rect(a, l):
                a.kill()
                l.kill()
                pygame.event.post(pygame.event.Event(DESTROID))
    
            

def check_ship(ship, asteroid):
    ''' Checks for spaceship/asteroid collisions '''
    for s in ship:
        for a in asteroid:
            if pygame.sprite.collide_rect(s,a):
                s.damage += 1
                a.kill()
                if s.damage >= 3:
                    pygame.event.post(pygame.event.Event(MAX_DAMAGE))

'''----------------------------------LOOP-------------------------------'''
SPAWN_COUNT = 0
N = 20
GAME_ON = True
destroids = 0

while GAME_ON:
    SPAWN_COUNT += 1
    if SPAWN_COUNT % N == 0:
        asteroid_group.add(Asteroid('Assets/Asteroid_05.GIF', random.randrange(0, SCREEN_WIDTH)))
    if SPAWN_COUNT > 1000:
        SPAWN_COUNT = 0

    #Handling input (EVENTS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                laser_group.add(Laser(spaceship))
        if event.type == DESTROID:
            destroids += 1
        if event.type == MAX_DAMAGE:
            for ship in spaceship_group:
                GAME_ON = False
                print(destroids)
                ship.kill()
                screen.fill('red')
                pygame.display.flip()
                pygame.time.wait(3000)
                break


    # Drawing Collisions
    check_laser(laser_group, asteroid_group)
    check_ship(spaceship_group, asteroid_group)

    # Updating the window (This could, in theory, be a function. )
    pygame.display.flip()
    screen.fill(background)

    asteroid_group.draw(screen)
    spaceship_group.draw(screen)
    laser_group.draw(screen)

    laser_group.update()
    asteroid_group.update()
    spaceship_group.update()

    clock.tick(60)
