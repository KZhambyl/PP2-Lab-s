import sys, pygame, datetime, math
pygame.init()

size = w,h = 1000,800
background = pygame.image.load("images/mainclock.png")
bg_rect = background.get_rect(center=(w//2,h//2))
la_start = pygame.image.load("images/leftarm.png")
ra_start = pygame.image.load("images/rightarm.png")
ra_start = pygame.transform.rotate(ra_start, -46)
screen = pygame.display.set_mode(size)

while 1:
    for event in pygame.event.get():
        if event.type==pygame.QUIT: sys.exit()

    current_time = datetime.datetime.today()
    minute = current_time.minute
    second = current_time.second

    min_ang = minute *(-6)
    sec_ang = second * (-6)

    ra = pygame.transform.rotate(ra_start, min_ang)
    la = pygame.transform.rotate(la_start, sec_ang)

    ra_rect=ra.get_rect(center=(w//2,h//2))
    la_rect = la.get_rect(center=(w//2,h//2))

    dy = 17 * math.sin(sec_ang*math.pi/180)
    dx = 17 * math.cos(sec_ang*math.pi/180) * math.cos(sec_ang*math.pi/180)

    la_rect.x += dx
    la_rect.y += dy

    screen.fill('black')
    screen.blit(background,bg_rect)
    screen.blit(la,la_rect)
    screen.blit(ra,ra_rect)
    pygame.display.flip()