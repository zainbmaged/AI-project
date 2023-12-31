import pygame
import trail
import copy
import pprint
#button class
class Button():
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, surface):
		action = False
              
          
        
		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True
                

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button on screen
		surface.blit(self.image, (self.rect.x, self.rect.y))
        
		return action
def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

#Pygame Setup
pygame.init()
screen = pygame.display.set_mode((800, 700))
#Game Window Title
pygame.display.set_caption("Gobblet Gobblers")
#Change Icon
pygame_icon = pygame.image.load('gobblet.png')
pygame.display.set_icon(pygame_icon)
clock = pygame.time.Clock()
running = True
state = 'main-window'
game_paused = False

new_img = pygame.image.load("button_newgame.png").convert_alpha()
new_button = Button(610, 240, new_img, 1)

quit_img = pygame.image.load("button_quit.png").convert_alpha()
quit_button = Button(600, 500, quit_img, 1)

restart_img = pygame.image.load("button_restart.png").convert_alpha()
restart_button = Button(600, 410, restart_img, 1)

pause_img = pygame.image.load("button_pause.png").convert_alpha()
pause_button = Button(600, 320, pause_img, 1)

start_img = pygame.image.load("button_start.png").convert_alpha()
start_button = Button(580, 600, start_img, 1)
 
gobblet_img = pygame.image.load("gobblet.png")

row = 5
col = 5

brown =(165, 164, 135)
white = (255,255,255)
black = (0,0,0)

def initializeBoard():
    global board
    board = [[[0 ] for j in range(row)] for i in range(col)]
    board[1][0] = [0,1,3,5,7]
    board[2][0] = [0,1,3,5,7]
    board[3][0] = [0,1,3,5,7]
    board[0][1] = [0,2,4,6,8]
    board[0][2] = [0,2,4,6,8]
    board[0][3] = [0,2,4,6,8]
    wins=None
selected = None
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
            #draw grid with white squares 
            pygame.draw.rect(screen, black, (c*120, r*120,240,240), 1)

    for r in range(row):
        for c in range(col):	
            for s in range(len(board[r][c])):	
                if board[r][c][s]==2 or board[r][c][s]==4 or board[r][c][s]==6 or board[r][c][s]==8:	
                    pygame.draw.circle(screen, white, ((120*c)+60,(120*r)+60), board[r][c][s]*6.5)
                if board[r][c][s]==1 or board[r][c][s]==3 or board[r][c][s]==5 or board[r][c][s]==7:	
                    pygame.draw.circle(screen, black, ((120*c)+60,(120*r)+60),(board[r][c][s]+1)*6.5)
    if quit_button.draw(screen):
        running = False
    if restart_button.draw(screen):
        initializeBoard()
    if pause_button.draw(screen):
        game_paused = True
    if new_button.draw(screen):
       main_menu = True
    if selected:
        pc, pr = pygame.mouse.get_pos()    
        pygame.draw.circle(screen, turn, (pc, pr), (selected)*6.5)

    myfont = pygame.font.SysFont("monospace", 36, True)
   
    if wins==None:
        if turn == black:
            text=(myfont.render("Turn: Black", True, turn))
            screen.blit(text, (70, 610))
            pygame.display.flip()
        else:
            text=(myfont.render("Turn: White ", True, turn))
            screen.blit(text, (70, 610))
            pygame.display.flip()
    else:
        myfont = pygame.font.SysFont("monospace", 36, True)
        if wins == "White":
            text = (myfont.render(wins+" Player wins!!", True, white))
        else:
            text = (myfont.render(wins+" Player wins!!", True, black)) 
        screen.blit(text, (70, 610))
        pygame.display.flip()
   
                
flag = False

initializeBoard()
main_menu=True

player_1 = None
player_2 = None

while running:
    #Poll for events
    temp=0
    update_required = False
    render()
    while main_menu == True:
        screen.fill((196, 164, 132))
        screen.blit(pygame.transform.scale(gobblet_img, (100,100)), (350,23)) 
        draw_text("Gobblet ", pygame.font.SysFont("arialblack", 45), (248, 111, 3), 198, 120)
        draw_text("Gobblers", pygame.font.SysFont("arialblack", 45), (52, 76, 235), 400, 120)
        draw_text("Player 1:", pygame.font.SysFont("arialblack", 45), (255, 255, 255), 90, 250)
        draw_text("Human", pygame.font.SysFont("arialblack", 40), (255, 255, 255), 380, 250)
        if player_1 != "Human" or player_1 == None:
            pygame.draw.circle(screen, (0,0,0), (560,284), 20, 3)
        draw_text("AI", pygame.font.SysFont("arialblack", 40), (255, 255, 255), 650, 250)
        if player_1 == "Human":
            pygame.draw.circle(screen, (0,0,0), (560,284), 20, 3)
            pygame.draw.circle(screen, (0,0,255), (560,284), 17)
        if player_1 != "AI" or player_1 == None:
            pygame.draw.circle(screen, (0,0,0), (724,284), 20, 3)
        if player_1 == "AI":
            pygame.draw.circle(screen, (0,0,0), (724,284), 20, 3)
            pygame.draw.circle(screen, (0,0,255), (724,284), 17)
        draw_text("Player 2:", pygame.font.SysFont("arialblack", 45), (0,0,0), 90, 450)
        draw_text("Human", pygame.font.SysFont("arialblack", 40), (0,0,0), 380, 450)
        if player_2 != "Human" or player_2 == None:
            pygame.draw.circle(screen, (0,0,0), (560,484), 20, 3)
        if player_2 == "Human":
            pygame.draw.circle(screen, (0,0,0), (560,484), 20, 3)
            pygame.draw.circle(screen, (0,0,255), (560,484), 17)           
        draw_text("AI", pygame.font.SysFont("arialblack", 40), (0,0,0), 650, 450)
        if player_2 != "AI" or player_2 == None:
            pygame.draw.circle(screen, (0,0,0), (724,484), 20, 3)
        if player_2 == "AI":
            pygame.draw.circle(screen, (0,0,0), (724,484), 20, 3)
            pygame.draw.circle(screen, (0,0,255), (724,484), 17)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                main_menu = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = False
                    main_menu = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if y > 700:
                    continue
                if x > 800:
                    continue
                if 264 <= y <= 304 and 540 <= x <= 580:
                    player_1 = "Human"

                if 264 <= y <= 304 and 704 <= x <= 744:
                    player_1 = "AI"

                if 464 <= y <= 504 and 540 <= x <= 580:
                    player_2 = "Human"

                if 464 <= y <= 504 and 704 <= x <= 744:
                    player_2 = "AI"
            
        if start_button.draw(screen):
            #mode variable here
            if (player_1 != None) and (player_2 != None):
                main_menu = False

        pygame.display.flip()
            
    while game_paused == True:
        screen.fill((52, 78, 91))
        draw_text("Game paused press Space to resume", pygame.font.SysFont("arialblack", 35), (255, 255, 255), 50, 320)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                game_paused = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_paused = False
    if (player_1=="AI" and turn == white) or(player_2=="AI" and turn == black):
        pprint.pprint(board)
        if( (player_1=="AI" and turn == white)):
                maximizer =True
                minmax_output=trail.minimax(board,4,maximizer,-10000,10000)
        if((player_2=="AI" and turn == black)):
             maximizer =False
             minmax_output=trail.minimax(board,4,maximizer,-10000,10000)
        
        pprint.pprint(board)
        
        if(len(minmax_output)>3):
            ay=minmax_output[4]
            ax=minmax_output[5]  
            if (board[ay][ax][-1]!=0) :
                
                select= board[ay][ax][-1]
                board[ay][ax].pop() 
                ay=minmax_output[2]
                ax=minmax_output[3] 
                 
                board[ay][ax].append(select)
        
        win()
        nextturn()                           
        render()

    

    else:
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                
                    x, y = event.pos
                    if y > 700:
                        continue
                    if x > 800:
                        continue
                    gx = (x*col)//600
                    gy = (y*row)//600
                    if gx <= 4 and gy <= 4:
                        piece = board[gy][gx][-1]
                    else:
                        piece = 0
                    if selected:
                            if 1 <= gy < row and  1 <= gx < col:
                                if board[gy][gx][-1] %2==1 and selected%2==0:
                                    temp=board[gy][gx][-1]+1
                                else:
                                    temp=board[gy][gx][-1]
                                if temp < selected:
                                    if turn == black:
                                        if flag == True and board[gy][gx][-1] != 0 and board[gy][gx][-1] % 2 == 0:
                                            count=0
                                            #check 3 in a row
                                            for i in range(1,5):
                                                if board[gy][i][-1]%2==0 and board[gy][i][-1] !=0:
                                                    count=count+1
                                            if count==3  or (count>3  and (gx !=gx_old or gy !=gy_old)):
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
                                            if count==3  or (count>3  and (gx !=gx_old or gy !=gy_old)):
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
                                                if count==3  or (count>3  and (gx !=gx_old or gy !=gy_old)):
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
                                                if count==3  or (count>3  and (gx !=gx_old or gy !=gy_old)):
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
                                            flag = False
                                    else:
                                      if board[gy][gx][-1] < selected:
                                        if flag == True and board[gy][gx][-1]%2==1:
                                            count=0
                                            #check 3 in a row
                                            for i in range(1,5):
                                                if board[gy][i][-1]%2==1 :
                                                    count=count+1
                                            if count==3  or (count>3  and (gx !=gx_old or gy !=gy_old)):
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
                                            if count==3  or (count>3  and (gx !=gx_old or gy !=gy_old)):
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
                                                if count==3  or (count>3  and (gx !=gx_old or gy !=gy_old)):
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
                                                if count==3  or (count>3  and (gx !=gx_old or gy !=gy_old)):
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
                        if turn == black and piece % 2 == 1 and player_2 =="Human" and  board[gy][gx][-1]!=0:
                            selected = piece+1
                            board[gy][gx].pop()
                        if turn == white and piece % 2 == 0 and piece != 0 and player_1 =="Human" and board[gy][gx][-1]!=0:
                            selected = piece
                            board[gy][gx].pop()
                        if 1 <= gx < col and 1 <= gy < row:     #piece removed from inside board
                            flag = True
                            gx_old = gx
                            gy_old = gy
                        
                        update_required = True

                
 
    if selected or update_required:
        render() 

    if quit_button.draw(screen):
        running = False
    if restart_button.draw(screen):
        wins=None
        if turn == black:
            nextturn()
        render()
        initializeBoard()
    if pause_button.draw(screen):
        game_paused = True
    if new_button.draw(screen):
        wins=None
        player_1=None
        player_2=None
        if turn == black:
            nextturn()
        render()
        initializeBoard()
        main_menu = True
    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

pygame.quit()