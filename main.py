import pygame
from pygame import image
import numpy as np
import pprint

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 700))
clock = pygame.time.Clock()
running = True
state = 'main-window'


row = 5
col = 5

brown =(165, 164, 135)
white = (255,255,255)
black = (0,0,0)

n = 5
board = [[[0 ] for j in range(n)] for i in range(n)]

board[1][0]=[0,1,3,5,7]
board[2][0]=[0,1,3,5,7]
board[3][0]=[0,1,3,5,7]


board[0][1]=[0,2,4,6,8]
board[0][2]=[0,2,4,6,8]
board[0][3]=[0,2,4,6,8]

pprint.pprint(board)



selected=None
turn = white

def nextturn():
    global turn
    if turn == white:
        turn = black
    elif turn == black:
        turn = white
wins=None
def win():
                             #check 3 in a row
                                global wins   
                                
                                for i in range(1,5):
                                    count=0
                                    for j in range(1,5):
                                        if board[i][j][-1]%2==0 and board[i][j][-1] !=0:
                                           count=count+1
                                    if count>3:
                                         wins="White"
                                         
                                    
                                
                                for i in range(1,5):
                                    count=0
                                    for j in range(1,5):
                                     if board[j][i][-1]%2==0 and board[j][i][-1] !=0:
                                        count=count+1
                                    if count>3:
                                        wins="White"
                                    
                                #check 3 in a positive main diagonal
                               
                                count=0
                                for i in range(1,5):
                                        if board[i][i][-1]%2==0 and board[i][i][-1] !=0:
                                            count=count+1
                                if count>3:
                                        wins="White"
                                        
                                #check 3 in a negative main diagonal
                                
                                count=0
                                for i in range(1,5):
                                        if board[i][5-i][-1]%2==0 and board[i][5-i][-1] !=0:
                                            count=count+1
                                if count>3:
                                        wins="White"


                                 #check 3 in a row
                                
                                for i in range(1,5):
                                    count=0
                                    for j in range(1,5):
                                        if board[j][i][-1]%2==1 :
                                           count=count+1
                                    if count>3:
                                        wins="Black"
                                    
                                
                                for i in range(1,5):
                                    count=0
                                    for j in range(1,5):
                                     if board[i][j][-1]%2==1:
                                        count=count+1
                                    if count>3:
                                        wins="Black"
                                    
                                #check 3 in a positive main diagonal
                               
                                count=0
                                for i in range(1,5):
                                        if board[i][i][-1]%2==1:
                                            count=count+1
                                if count>3:
                                        wins="Black"
                                        
                                #check 3 in a negative main diagonal
                                
                                count=0
                                for i in range(1,5):
                                        if board[i][5-i][-1]%2==1:
                                            count=count+1
                                if count>3:
                                        wins="Black"
                                
                                        
def render():
    
    screen.fill((196, 164, 132))
    for r in range(1,row-1):
        for c in range(1,col-1):
            
           
       ## draw grid with white squares 
                pygame.draw.rect(screen, black, (c*120, r*120,240,240), 1)

    for r in range(row):
          for c in range(col):	
                    for s in range(len(board[r][c])):	
                     if board[r][c][s]==2 or board[r][c][s]==4 or board[r][c][s]==6 or board[r][c][s]==8:	
                        
                 
                        pygame.draw.circle(screen, white, ((120*c)+60,(120*r)+60), board[r][c][s]*6.5)
                    if board[r][c][s]==1 or board[r][c][s]==3 or board[r][c][s]==5 or board[r][c][s]==7:	
                        
                 
                        pygame.draw.circle(screen, black, ((120*c)+60,(120*r)+60),(board[r][c][s]+1)*6.5)
    
    if selected:
     pc, pr = pygame.mouse.get_pos()    
       
     
     
  
     pygame.draw.circle(screen, turn, (pc, pr), (selected)*6.5)  
    myfont = pygame.font.SysFont("monospace", 36)
   
    if wins==None:
        if turn == black:
            text=(myfont.render("Turn: Black", True, turn))
            screen.blit(text, (70, 610))
            pygame.display.flip()
        else:
            text=(myfont.render("Turn: White ", True, turn))
            screen.blit(text, (70, 610))
            pygame.display.flip()
    else :
                
                myfont = pygame.font.SysFont("monospace", 36)
                if wins == "White":
                    text=(myfont.render(wins+" Player wins!!", True, white))
                else:
                    text=(myfont.render(wins+" Player wins!!", True, black)) 
                screen.blit(text, (70, 610))
                pygame.display.flip()
                
    
flag=False

while running:
    # poll for events
    update_required = False
    
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
   
        # fill the screen with a color to wipe away anything from last frame
        render()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if y > 700:
                continue
            gx = x*col//600
            gy =(y*row)//600
            if gx<5 and gy<5:
             piece = board[gy][gx][-1]
            else:
                piece =0

            if selected:
                if 1 <= gy <= row and board[gy][gx][-1]< selected and  1 <= gx <= row :
                        if turn  == black  :
                            if flag ==True and board[gy][gx][-1] !=0 and board[gy][gx][-1]%2==0:
                                count=0
                                #check 3 in a row
                                for i in range(1,5):
                                    if board[gy][i][-1]%2==0 and board[gy][i][-1] !=0:
                                        count=count+1
                                if count==3  or (count>3  and gx !=gx_old and gy !=gy_old):
                                    board[gy][gx].append(selected-1)
                                    selected = None
                                    win()
                                    nextturn()
                                    update_required = True
                                    flag=False
                                    
                                
                                count=0
                            
                                #check 3 in a colum
                                for i in range(1,5):
                                    if board[i][gx][-1]%2==0 and board[i][gx][-1] !=0:
                                        count=count+1
                                if count==3  or (count>3  and gx !=gx_old and gy !=gy_old):
                                    board[gy][gx].append(selected-1)
                                    selected = None
                                    win()
                                    nextturn()
                                    update_required = True
                                    flag=False
                                
                                #check 3 in a positive main diagonal
                                if gy == gx:
                                    count=0
                                    for i in range(1,5):
                                        if board[i][i][-1]%2==0 and board[i][i][-1] !=0:
                                            count=count+1
                                    if count==3  or (count>3  and gx !=gx_old and gy !=gy_old):
                                        board[gy][gx].append(selected-1)
                                        selected = None
                                        win()
                                        nextturn()
                                        update_required = True
                                        flag=False
                                    #check 3 in a negative main diagonal
                                if 5- gy == gx:
                                    count=0
                                    for i in range(1,5):
                                        if board[i][5-i][-1]%2==0 and board[i][5-i][-1] !=0:
                                            count=count+1
                                    if count==3  or (count>3  and gx !=gx_old and gy !=gy_old):
                                        board[gy][gx].append(selected-1)
                                        selected = None
                                        win()
                                        nextturn()
                                        update_required = True
                                        flag=False
                                   
                            else:
                             board[gy][gx].append(selected-1)
                             selected = None
                             win()
                             nextturn()
                             update_required = True
                             flag=False
                        else:
                              if flag ==True and  board[gy][gx][-1]%2==1:
                                count=0
                                #check 3 in a row
                                for i in range(1,5):
                                    if board[gy][i][-1]%2==1 :
                                        count=count+1
                                if count==3  or (count>3  and gx !=gx_old and gy !=gy_old):
                                    board[gy][gx].append(selected)
                                    selected = None
                                    win()
                                    nextturn()
                                    update_required = True
                                    flag=False
                                
                                count=0
                            
                                #check 3 in a colum
                                for i in range(1,5):
                                    if board[i][gx][-1]%2==1:
                                        count=count+1
                                if count==3  or (count>3  and gx !=gx_old and gy !=gy_old):
                                    board[gy][gx].append(selected)
                                    selected = None
                                    win()
                                    nextturn()
                                    update_required = True
                                    flag=False
                                
                                #check 3 in a positive main diagonal
                                if gy == gx:
                                    count=0
                                    for i in range(1,5):
                                        if board[i][i][-1]%2==1 :
                                            count=count+1
                                    if count==3  or (count>3  and gx !=gx_old and gy !=gy_old):
                                        board[gy][gx].append(selected)
                                        selected = None
                                        win()
                                        nextturn()
                                        update_required = True
                                        flag=False
                                #check 3 in a negative main diagonal
                                if 5- gy == gx:
                                    count=0
                                    for i in range(1,5):
                                        if board[i][5-i][-1]%2==1 :
                                            count=count+1
                                    if count==3  or (count>3  and gx !=gx_old and gy !=gy_old):
                                            board[gy][gx].append(selected)
                                            selected = None
                                            win()
                                            nextturn()
                                            update_required = True
                                            flag=False
                              else:
                                board[gy][gx].append(selected)
                                selected = None
                                win()
                                nextturn()
                                update_required = True
                                flag=False
                    
                        
                        
            else:
                if piece == 0:
                    continue
                if turn  == black and piece % 2 ==1:
                    selected = piece+1
                    board[gy][gx].pop()
                if turn  == white and piece % 2 ==0 and piece !=0:
                    selected = piece
                    board[gy][gx].pop()
                print(gx,gy)
                if 1 <= gx <= row and 1 <= gy <= row :##piece removed from inside board
                    flag=True
                    gx_old=gx
                    gy_old=gy
               
                
                pprint.pprint(board)
                update_required = True

    if selected or update_required:
                render()   
           
    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()

