import sys, pygame
pygame.init()

W, H = 800, 600
screen = pygame.display.set_mode((W,H))
screen.fill('gray')
font = pygame.font.SysFont(None, 100)
play_button = font.render("play", 1, 'yellow','black')
pl_rect = play_button.get_rect(centerx=W//2)
stop_button = font.render("stop", 1, 'yellow','black')
st_rect = stop_button.get_rect(centerx=W//2, bottom=H)
next_button = font.render("next", 1, 'yellow', 'black')
ne_rect = next_button.get_rect(centery=H//2, right=W)
prev_button = font.render("prev", 1, 'yellow', 'black')
pr_rect = prev_button.get_rect(centery=H//2, left=0)

playlist = ["sounds/sound1.mp3","sounds/sound2.mp3","sounds/sound3.mp3"]
i=0
pygame.mixer.music.load("sounds/sound1.mp3")
pygame.mixer.music.play(0)
pygame.mixer.music.pause()

screen.blit(play_button,pl_rect)
screen.blit(stop_button,st_rect)
screen.blit(next_button,ne_rect)
screen.blit(prev_button,pr_rect)
pygame.display.update()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button==1:
            if pygame.mouse.get_focused and pl_rect.collidepoint(pygame.mouse.get_pos()): pygame.mixer.music.unpause()
            elif pygame.mouse.get_focused and st_rect.collidepoint(pygame.mouse.get_pos()): pygame.mixer.music.pause()
            elif pygame.mouse.get_focused and pr_rect.collidepoint(pygame.mouse.get_pos()): 
                if i>1: i-=1 
                else: i=0
                i = i%3
                pygame.mixer.music.load(playlist[i])
                pygame.mixer.music.play(0)
            elif pygame.mouse.get_focused and ne_rect.collidepoint(pygame.mouse.get_pos()): 
                i+=1
                i = i%3
                pygame.mixer.music.load(playlist[i])
                pygame.mixer.music.play(0)
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_SPACE: pygame.mixer.music.unpause()
            elif event.key==pygame.K_s: pygame.mixer.music.pause()
            elif event.key==pygame.K_LEFT: 
                if i>1: i-=1 
                else: i=0
                i = i%3
                pygame.mixer.music.load(playlist[i])
                pygame.mixer.music.play(0)
            elif event.key==pygame.K_RIGHT:
                i+=1
                i = i%3
                pygame.mixer.music.load(playlist[i])
                pygame.mixer.music.play(0)

# Create music player with keyboard controller. You have to be able to press keyboard: 
# play, stop, next and previous as some keys. Player has to react to the given command appropriately.