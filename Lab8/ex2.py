import pygame,sys,random,time
pygame.init()
# cell size 20,20. Level increases every 3 scores

# basic settings
W,H = 800,600
screen = pygame.display.set_mode((W,H))
background = pygame.surface.Surface((W,H))
background.fill('brown')
pygame.draw.rect(background,'black',(20,40,W-40,H-60))
font = pygame.font.SysFont('comicsansms', 40)
clock =pygame.time.Clock()
FPS = 10

# snake
speed = 20
direction = (0,0)
length = 1
snake = pygame.rect.Rect(random.randint(1,38)*20, random.randint(2,28)*20,20,20)
particles = [snake.copy()]
level = 1

# food
score = 0
while True:
    food = pygame.rect.Rect(random.randint(1,38)*20, random.randint(2,28)*20,20,20)
    if food!=snake: break

# game loop
while 1:
    for event in pygame.event.get():
        if event.type==pygame.QUIT: sys.exit()
        # snake movement
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT and direction!=(-speed,0): direction = (speed,0)
            elif event.key==pygame.K_LEFT and direction!=(speed,0): direction = (-speed,0)
            elif event.key==pygame.K_UP and direction!=(0,speed): direction = (0,-speed)
            elif event.key==pygame.K_DOWN and direction!=(0,-speed): direction = (0,speed)
    snake.move_ip(direction)
    # list of particles of snake
    particles.append(snake.copy())
    particles=particles[-length:]
    level = 1+score//3
    # collision between particles of snake
    self_collision = pygame.Rect.collidelist(snake,particles[:-1]) != -1
    # food collision
    if(snake.bottomleft==food.bottomleft):
        food = pygame.rect.Rect(random.randint(1,38)*20, random.randint(2,28)*20,20,20)
        score+=1
        length+=1
    # border collision or selfcollision
    elif(snake.x>W-40 or snake.x<20 or snake.y<40 or snake.y>H-40) or self_collision: 
        # Game over screen
        lose = font.render("You Lose!",1,'Yellow')
        screen.fill('black')
        screen.blit(lose,lose.get_rect(center=(W//2,H//2)))
        pygame.display.update()
        # Setting all values
        snake = pygame.rect.Rect(random.randint(1,38)*20, random.randint(2,28)*20,20,20)
        while True:
            food = pygame.rect.Rect(random.randint(1,38)*20, random.randint(2,28)*20,20,20)
            if food!=snake: break
        score=0
        direction=(0,0)
        length=1
        time.sleep(2)

    # drawing all objects
    screen.blit(background,(0,0))
    if level==0: level=1
    # score and level indicators
    score_tab = font.render(f"Score: {score}",1,'yellow')
    level_tab = font.render(f"Level: {level}",1,'yellow')
    screen.blit(score_tab,score_tab.get_rect(center=(100,16)))
    screen.blit(level_tab,level_tab.get_rect(center=(W-100,16)))
    # drawing all particles of snake
    pygame.draw.rect(screen,'yellow', (food.x,food.y,20,20))
    [pygame.draw.rect(screen,'green', particle) for particle in particles]

    pygame.display.update()
    clock.tick(FPS*level)