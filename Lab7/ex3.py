import sys, pygame
pygame.init()

size = width, height = 800, 600
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
x, y = 400, 300
speed = 20
toLeft = toRight = toUp = toDown = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN: toDown=True
            elif event.key == pygame.K_UP: toUp=True
            if event.key == pygame.K_LEFT: toLeft=True
            elif event.key == pygame.K_RIGHT: toRight=True
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT,pygame.K_RIGHT]: toLeft = toRight = False
            if event.key in [pygame.K_UP,pygame.K_DOWN]: toUp = toDown = False
    if toLeft and x>25: x-=speed
    elif toRight and x<width-25: x+=speed
    if toUp and y>25: y-=speed
    elif toDown and y<height-25: y+=speed

    screen.fill('white')
    pygame.draw.circle(screen, 'red', (x,y), 25)
    pygame.display.update()
    clock.tick(60)


# Draw circle - a red ball of size 50 x 50 (radius = 25) on white background. 
# When user presses Up, Down, Left, Right arrow keys on keyboard, the ball should 
# move by 20 pixels in the direction of pressed key. The ball should not leave the 
# screen, i.e. user input that leads the ball to leave of the screen should be ignored.