import pygame, sys, random
'''---------------------------------CLASS CODE/SPRITES--------------------'''
class Blob(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('Assets/sprite_0.png'), (150, 150))
        self.rect = self.image.get_rect()

        self.sprite_count = 0

    def update(self):
        self.handle_keys()
        self.image = pygame.transform.scale(pygame.image.load(f'Assets/sprite_{self.sprite_count}.png'), (150, 150))
        self.sprite_count += 1
        if self.sprite_count > 3: self.sprite_count = 0

    def handle_keys(self):
        """ Handles Keys """
        key = pygame.key.get_pressed()
        dist = 15 # distance moved in 1 frame
        if key[pygame.K_DOWN]: # down key
            self.rect.y += dist # move down
        elif key[pygame.K_UP]: # up key
            self.rect.y -= dist # move up
        if key[pygame.K_RIGHT]: # right key
            self.rect.x += dist # move right
        elif key[pygame.K_LEFT]: # left key
            self.rect.x -= dist # move left

class Asteroid(pygame.sprite.Sprite):
    '''Asteroid sprite -- essentially just moves down the screen. '''
    def __init__(self, picture_path, pos_x):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(picture_path), (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, 0]

    def update (self):
        self.rect.y += 5
'''---------------------------------SETUP-------------------------------'''
# General setup
pygame.init()
clock = pygame.time.Clock()

# Setting up the main window
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Game Title')

# Sounds
crash = pygame.mixer.music.load('Assets/Grenade+1.mp3')

#BLOB

blob_1 = Blob()
blob_group = pygame.sprite.Group()
blob_group.add(blob_1)

#Asteroids
asteroid = Asteroid('Assets/Asteroid_05.GIF', random.randrange(0, screen_width))
asteroid_group = pygame.sprite.Group()
asteroid_group.add(asteroid)

def check_collision(asteroid, blob):
    for a in asteroid:
        for b in blob:
            if pygame.sprite.collide_rect(a,b):
                #pygame.mixer.music.play()
                pygame.mixer.Sound('Assets/Grenade+1.mp3').play()

'''----------------------------------LOOP-------------------------------'''
SPAWN_COUNT = 0
N = 20
while True:
    SPAWN_COUNT += 1
    if SPAWN_COUNT % N == 0:
        asteroid_group.add(Asteroid('Assets/Asteroid_05.GIF', random.randrange(0, screen_width)))
    if SPAWN_COUNT > 1000:
        SPAWN_COUNT = 0
        
    #Handling input (EVENTS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
            sys.exit()

    #Checking for collisions

    check_collision(asteroid_group, blob_group)

    # Drawing
    screen.fill('black')
    blob_group.draw(screen)
    asteroid_group.draw(screen)

    # Updating the window 
    blob_group.update()
    asteroid_group.update()
    pygame.display.flip()
    clock.tick(60)