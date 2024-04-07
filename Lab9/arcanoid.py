import pygame 
import random
pygame.init()

W, H = 1200, 800
FPS = 60

screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
clock = pygame.time.Clock()
done = False
bg = (0, 0, 0)

#paddle
paddleW = 150
paddleH = 25
paddleSpeed = 20
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)


#Ball
ballRadius = 20
ballSpeed = 6
ball_rect = int(ballRadius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
dx, dy = 1, -1

#Game score
game_score = 0
game_score_fonts = pygame.font.SysFont('comicsansms', 40)
game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (0, 0, 0))
game_score_rect = game_score_text.get_rect(center = (210, 20))

#Catching sound
collision_sound = pygame.mixer.Sound('sounds/catch.mp3')

def detect_collision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    if delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy


#block settings
block_list = [pygame.Rect(10 + 120 * i, 50 + 70 * j, 100, 50) for i in range(10) for j in range (4)]
color_list = [(random.randrange(0, 255), random.randrange(0, 255),  random.randrange(0, 255)) for i in range(10) for j in range(4)] 
print(block_list)
 
# unbreakable blocks 
unbreak_color = (77,74,74)
unbreakable_block = pygame.surface.Surface((100,50))
unbreakable_block.fill(unbreak_color)
unbreak_blocks_count = 5
unbreakable_blocks = [pygame.Rect(10 + 120*random.randint(0,9), 50 + 70 * random.randint(0,3), 100, 50) for i in range(10)]
unbreakable_blocks = unbreakable_blocks[-unbreak_blocks_count:]

# bonus break
while 1:
    bonus_break_rect = pygame.Rect(10 + 120*random.randint(0,9), 50 + 70 * random.randint(0,3), 100, 50)
    if bonus_break_rect not in unbreakable_blocks: break
bonus_break_color = (209,183,55)
bouns_break = pygame.surface.Surface((100,50))
bouns_break.fill(bonus_break_color)
bonus_earned = False


#Game over Screen
font = pygame.font.SysFont('comicsansms', 40)
losetext = font.render('Game Over', True, (255, 255, 255))
losetextRect = losetext.get_rect()
losetextRect.center = (W // 2, H // 2)

#Win Screen
wintext = font.render('You win yay', True, (0, 0, 0))
wintextRect = wintext.get_rect()
wintextRect.center = (W // 2, H // 2)

# Pause menu + settings
pauseMenu = pygame.surface.Surface((W,H))
bigfont = pygame.font.SysFont('comicsansms', 60)
pauseText = bigfont.render('Pause',1,'white')
settings = bigfont.render('settings',1,'white')
pauseMenu.blit(pauseText,pauseText.get_rect(centerx=W//2,y=10))
pauseMenu.blit(settings,settings.get_rect(centerx=W//2,y=200))
# ball color setting 
ballColor = 'red'
ballColors = ['red','purple','blue','green']
ballColorRects = [pygame.rect.Rect(i+500,295,40,40) for i in range(0,151,50)]
print("list: ",ballColorRects)
indx=0
for rect in ballColorRects:
    pygame.draw.rect(pauseMenu,ballColors[indx],rect)
    indx+=1
# paddle size setting 
paddleWlimit = 60
paddleHlimit = 10
text1 = font.render('Paddle size:',1,'white')
text2 = font.render('Ball color:',1,'white')
pauseMenu.blit(text1, text1.get_rect(x=300,centery=370))
pauseMenu.blit(text2, text2.get_rect(x=300,centery=310))
size1 = font.render('1x',1,'white')
size2 = font.render('1.5x',1,'white')
size3 = font.render('2x',1,'white')
size1Rect = size1.get_rect(x=540,centery=370)
size2Rect = size2.get_rect(x=600,centery=370)
size3Rect = size3.get_rect(x=700,centery=370)
pauseMenu.blit(size1,size1Rect)
pauseMenu.blit(size2,size2Rect)
pauseMenu.blit(size3,size3Rect)
pauseOn = False


# Increaing ball speed event
inc_speed = pygame.USEREVENT
pygame.time.set_timer(inc_speed,10000)
# Shrinking paddle event 
shrink_paddle = pygame.USEREVENT +1
pygame.time.set_timer(shrink_paddle,15000)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # Increaing ball speed 
        if event.type == inc_speed:
            ballSpeed*=1.2
        # Shrinking paddle
        if event.type == shrink_paddle:
            paddleW *= 0.9
            paddleH *=0.9
            if paddleW<paddleWlimit or paddleH<paddleHlimit: paddleW,paddleH = paddleWlimit,paddleHlimit
            paddle = pygame.rect.Rect(paddle.x,paddle.y, paddleW, paddleH)
        # Pause on/off
        if event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE: pauseOn = not pauseOn
    # Pause and setting process 
    while pauseOn:
        screen.blit(pauseMenu,(0,0))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type==pygame.QUIT: 
                done = True
                pauseOn = False
            if event.type==pygame.KEYDOWN: pauseOn = False
            if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                indx=0
                for color in ballColorRects:
                    if color.collidepoint(pygame.mouse.get_pos()): ballColor=ballColors[indx]
                    indx+=1
                if size1Rect.collidepoint(pygame.mouse.get_pos()): 
                    paddleW=150
                    paddleWlimit=60
                    center = paddle.center
                    paddle = pygame.rect.Rect(paddle.x,paddle.y, paddleW, 25)
                    paddle.center = center
                if size2Rect.collidepoint(pygame.mouse.get_pos()): 
                    paddleW=150*1.5
                    paddleWlimit=60*1.5
                    center = paddle.center
                    paddle = pygame.rect.Rect(paddle.x,paddle.y, paddleW, 25)
                    paddle.center = center
                if size3Rect.collidepoint(pygame.mouse.get_pos()): 
                    paddleW=150*2
                    paddleWlimit=60*2   
                    center = paddle.center
                    paddle = pygame.rect.Rect(paddle.x,paddle.y, paddleW, 25)
                    paddle.center = center

    screen.fill(bg)
    # print(next(enumerate(block_list)))

    #drawing blocks
    [pygame.draw.rect(screen, color_list[color], block) for color, block in enumerate (block_list)] 
    # drawing unbreakable blocks 
    for rect in unbreakable_blocks:
        screen.blit(unbreakable_block,rect)
    # drawing bonus break 
    if not bonus_earned:
        screen.blit(bouns_break,bonus_break_rect)

    pygame.draw.rect(screen, pygame.Color(255, 255, 255), paddle)
    pygame.draw.circle(screen, ballColor, ball.center, ballRadius)
    # print(next(enumerate (block_list)))

    #Ball movement
    ball.x += ballSpeed * dx
    ball.y += ballSpeed * dy

    #Collision left 
    if ball.centerx < ballRadius or ball.centerx > W - ballRadius:
        dx = -dx
    #Collision top
    if ball.centery < ballRadius + 50: 
        dy = -dy
    #Collision with paddle
    if ball.colliderect(paddle) and dy > 0:
        dx, dy = detect_collision(dx, dy, ball, paddle)

    #Collision blocks
    hitIndex = ball.collidelist(block_list)
    if hitIndex != -1:
        if block_list[hitIndex] in unbreakable_blocks:
            dx, dy = detect_collision(dx, dy, ball, block_list[hitIndex])
        else:
            # bonus break effect
            if block_list[hitIndex]==bonus_break_rect:
                center = paddle.center
                paddle = pygame.rect.Rect(paddle.x,paddle.y, 200, 25)
                paddle.center = center
                bonus_earned = True
            hitRect = block_list.pop(hitIndex)
            hitColor = color_list.pop(hitIndex)
            dx, dy = detect_collision(dx, dy, ball, hitRect)
            game_score += 1
            collision_sound.play()
        
    #Game score
    game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (255, 255, 255))
    screen.blit(game_score_text, game_score_rect)
    
    #Win/lose screens
    if ball.bottom > H:
        screen.fill((0, 0, 0))
        screen.blit(losetext, losetextRect)
    elif len(block_list)==5:
        screen.fill((255,255, 255))
        screen.blit(wintext, wintextRect)
    #Paddle Control
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        paddle.left -= paddleSpeed
    if key[pygame.K_RIGHT]:
        paddle.right += paddleSpeed
    if paddle.left<0: paddle.left=0
    if paddle.right>W: paddle.right=W


    pygame.display.flip()
    clock.tick(FPS)
