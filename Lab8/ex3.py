import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    x = 0
    y = 0
    rect_mode = False
    circle_mode = False
    erase_mode = False
    points = []
    cor_x=0
    painting_color = 'black'

    class Color(pygame.sprite.Sprite):
        def __init__(self,color,cor_x):
            super().__init__()
            self.color = color
            self.col_x=cor_x
            self.col_y=70
        def draw(self):
            pygame.draw.rect(screen,self.color,(self.col_x,0,100,self.col_y))

    colors = pygame.sprite.Group()
    col_names = ['red','green','blue','yellow','purple','pink','gray','black']
    for i in range(8):
        colors.add(Color(col_names[i], cor_x))
        cor_x+=100


    st_pos = None
    
    while True:
        
        pressed = pygame.key.get_pressed()
        mouse_pr = pygame.mouse.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            
            # determine if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT: return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held: return
                if event.key == pygame.K_F4 and alt_held: return
                if event.key == pygame.K_ESCAPE: return

                # mode keys
                if event.key == pygame.K_r: 
                    rect_mode = not rect_mode
                    circle_mode = False
                    erase_mode = False
                if event.key == pygame.K_c: 
                    circle_mode = not circle_mode
                    rect_mode = False
                    erase_mode = False
                if event.key == pygame.K_e: 
                    erase_mode = not erase_mode 
                    rect_mode = False
                    circle_mode = False
            
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1: st_pos = None

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pressed[pygame.K_a]:
                    st_pos = event.pos

                if event.button == 1: # left click grows radius
                    radius = min(200, radius + 1)
                    
                    # switching color by LBM click
                    for cur_color in colors:
                        rect = pygame.Rect(cur_color.col_x,0,100,cur_color.col_y)
                        if rect.collidepoint(position): 
                            painting_color = cur_color.color
                            st_pos=None

                elif event.button == 3: # right click shrinks radius
                    radius = max(1, radius - 1)

                
            
            if event.type == pygame.MOUSEMOTION:
                # if mouse moved, add point to list
                position = event.pos
                points = points + [position]
                points = points[-256:]
                
                # drawing modes
                if mouse_pr[0]:
                    if rect_mode:
                        if st_pos is None: st_pos = position
                        pygame.draw.rect(screen, painting_color, (st_pos[0], st_pos[1],position[0]-st_pos[0],position[1]-st_pos[1]))
                        pygame.display.update()
                    if circle_mode:
                        if st_pos is None: st_pos = position
                        pygame.draw.circle(screen,painting_color,st_pos, event.pos[0]-st_pos[0])
                        pygame.display.update()
                    if erase_mode:
                        pygame.draw.circle(screen, 'white', position, 25)
                        pygame.display.update()

                


        # draw all points
        if not rect_mode and not circle_mode and not erase_mode :
            screen.fill('white')
            i = 0
            while i < len(points) - 1:
                drawLineBetween(screen, i, points[i], points[i + 1], radius, painting_color)
                i += 1
        
        for col in colors:
            col.draw()

        pygame.display.flip()
        clock.tick(60)

def drawLineBetween(screen, index, start, end, width, painting_color):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, painting_color, (x, y), width)

main()


# Draw rectangle mode on/off - press R
# Draw circle mode on/off - hold C
# Eraser mode on/off - press E
# Color selection 