import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 480))
    screen.fill('white')
    clock = pygame.time.Clock()
    

    # modes 
    rect_mode = circle_mode = erase_mode = rhomb_mode = sqr_mode = equi_mode = right_mode = False
    
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
                    circle_mode = erase_mode = rhomb_mode = sqr_mode = equi_mode = right_mode = False
                    
                if event.key == pygame.K_c: 
                    circle_mode = not circle_mode
                    rect_mode = erase_mode = rhomb_mode = sqr_mode = equi_mode = right_mode = False

                if event.key == pygame.K_e: 
                    erase_mode = not erase_mode 
                    rect_mode = circle_mode = rhomb_mode = sqr_mode = equi_mode = right_mode = False

                if event.key == pygame.K_h: 
                    rhomb_mode = not rhomb_mode 
                    rect_mode = circle_mode = erase_mode = sqr_mode = equi_mode = right_mode = False

                if event.key == pygame.K_j: 
                    sqr_mode = not sqr_mode
                    rect_mode = circle_mode = erase_mode = rhomb_mode =equi_mode = right_mode = False

                if event.key == pygame.K_k: 
                    equi_mode = not equi_mode 
                    rect_mode = circle_mode = erase_mode = rhomb_mode = sqr_mode = right_mode = False

                if event.key == pygame.K_l: 
                    right_mode = not right_mode 
                    rect_mode = circle_mode = erase_mode = rhomb_mode = sqr_mode = equi_mode = False
                    
            
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1: 
                # drawing rhombus and triangles 
                if rhomb_mode:
                    end_pos = pygame.mouse.get_pos()
                    po_1 = (st_pos[0],(st_pos[1]+end_pos[1])/2)
                    po_2 = ((st_pos[0]+end_pos[0])/2,end_pos[1])
                    po_3 = (end_pos[0],(st_pos[1]+end_pos[1])/2)
                    po_4 = ((st_pos[0]+end_pos[0])/2,st_pos[1])
                    pygame.draw.polygon(screen,painting_color,(po_1,po_2,po_3,po_4))

                if equi_mode:
                    end_pos = pygame.mouse.get_pos()
                    po_1 = (st_pos[0],end_pos[1])
                    po_2 = end_pos
                    po_3 = ((st_pos[0]+end_pos[0])/2, st_pos[1])
                    pygame.draw.polygon(screen,painting_color,(po_1,po_2,po_3))

                if right_mode:
                    end_pos = pygame.mouse.get_pos()
                    po_1 = (st_pos[0],end_pos[1])
                    po_2 = end_pos
                    po_3 = ((st_pos[0]+end_pos[0])/2,(end_pos[1]-int((abs(end_pos[0]-st_pos[0]))*3**0.5/2)))
                    pygame.draw.polygon(screen,painting_color,(po_1,po_2,po_3))


                st_pos=None
                

            if event.type == pygame.MOUSEBUTTONDOWN:
                st_pos = event.pos
                # switching color by LBM click
                for cur_color in colors:
                    rect = pygame.Rect(cur_color.col_x,0,100,cur_color.col_y)
                    if rect.collidepoint(position): 
                        painting_color = cur_color.color

                
            
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
                    if sqr_mode:
                        if st_pos is None: st_pos = position
                        pygame.draw.rect(screen,painting_color, (st_pos[0], st_pos[1],position[0]-st_pos[0],position[0]-st_pos[0]))
                        pygame.display.update()

        
        for col in colors:
            col.draw()

        pygame.display.flip()
        clock.tick(60)


main()


# Draw rectangle mode on/off - press R
# Draw circle mode on/off - press C
# Eraser mode on/off - press E
# Color selection 

# Draw rhombus - press H
# Draw square - press J
# Draw equilateral triangle - press K
# Draw right triangle - press L