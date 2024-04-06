#Imports
import pygame, sys
from pygame.locals import *
import random, time

#Initialzing 
pygame.init()

#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()

#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0

# Adding background sound 
pygame.mixer.music.load("sounds/background.wav")
pygame.mixer.music.play(-1)

#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("images/AnimatedStreet.png")

#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("images/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)

      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("images/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
                  
# Coins class 
class Coin(pygame.sprite.Sprite):
    def __init__(self,weight,image, speed, _x, group):
        super().__init__()
        self.weight = weight
        self.image = pygame.image.load(image)
        self.image.set_colorkey('white')
        self.rect = self.image.get_rect(x=_x, y=0)
        self.speed = speed
        self.add(group)
    def update(self):
        if self.rect.y<SCREEN_HEIGHT:
            self.rect.y+=self.speed
        else: self.kill()


# Coins sprite group 
coins = pygame.sprite.Group()

# Coin images
coin_images = ["images/coin1.png","images/coin2.png","images/coin3.png"]
coin_weights = [150,300,200]
coin_speeds = [4,2,6]

# Coins score
coins_score = 0

def createCoin():
    x = random.randint(40, SCREEN_WIDTH-40)
    indx = random.randint(0,2)
    return Coin(coin_weights[indx],coin_images[indx],coin_speeds[indx],x, coins)

increased = False

#Setting up Sprites        
P1 = Player()
E1 = Enemy()

#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

#Game Loop
while True:
      
    #Cycles through all events occuring  
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.5      
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))

    # Random coin generator 
    if random.randint(0,100)<3 and len(coins)<3: createCoin()

    # Coins moving 
    coins.update()

    # Coins drawing 
    coins.draw(DISPLAYSURF)

    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)
        
    # Collision between coins and player 
    for coin in pygame.sprite.spritecollide(P1, coins, 1):
        coins_score+=coin.weight

    # Coin score indicator 
    coins_score_text = font_small.render(f"coins: {coins_score}",1,'yellow','black')
    coins_score_table = coins_score_text.get_rect(topright=(SCREEN_WIDTH-60,10))
    DISPLAYSURF.blit(coins_score_text,coins_score_table)

    # Increasing speed when player collects  2500 coins 
    if coins_score>=2500 and not increased:
        SPEED+=2
        increased = True

    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('sounds/crash.wav').play()
          time.sleep(1)
                   
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))
          
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()        
        
    pygame.display.update()
    FramePerSec.tick(FPS)
