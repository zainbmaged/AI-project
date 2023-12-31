import pygame

'''
MakeMove(board, piece, current_x, current_y, new_x, new_y)
If move is valid 
Make move and update board
If move is not valid
Return false
'''

def MakeMove(board, piece, current_x, current_y, new_x, new_y):     #y is the row and x is the column.
    move = False
    move1 = False
    coordinates = False
    selected = None
    myPiece = 0

    #Check if all coordinates are valid 
    if current_x >= 5 or current_y >= 5 or new_x >= 5 or new_y >= 5:
        move = False
    elif (current_x == 0 and current_y == 0) or (new_x == 0 and new_y == 0):
        move = False
    elif (current_x == 0 and current_y == 4) or (current_x == 4 and current_y == 0) or (new_x == 0 and new_y == 4) or (new_x == 4 and new_y == 0):
        move = False 
    elif not((1 <= new_x <= 4) and (1 <= new_y <= 4)):      #If the new coordinates to play are not on the board
        move = False
    else:
        coordinates = True
    
    #Check if the piece to be moved is outside the board
    if (current_x == 0 and 1 <= current_y <= 3) or (1 <= current_x <= 3 and current_y == 0):
        piece_on_board = False

    #Check if the piece to be moved is placed on the board
    if (1 <= current_x <= 4) and (1 <= current_y <= 4):
        piece_on_board = True
    
    if coordinates == True:
        if board[current_y][current_x][-1] == piece:
            myPiece = board[current_y][current_x][-1]
        else:
            myPiece = 0
    
    if myPiece == 0:
        pass
    if (myPiece % 2 == 1):
        selected = myPiece + 1
        move1 = True
    if (myPiece % 2 == 0) and (myPiece != 0):
        selected = myPiece
        move1 = True

    if selected:
        if (board[new_y][new_x][-1] % 2 == 1) and (selected % 2 == 0):
            temp = board[new_y][new_x][-1] + 1
        else:
            temp = board[new_y][new_x][-1]
        if temp < selected:
            if myPiece % 2 == 1:
                selected += 1
                if piece_on_board == True and board[new_y][new_x][-1] != 0 and board[new_y][new_x][-1] % 2 == 0:
                    count = 0
                    #check 3 in a row
                    for i in range(1,5):
                        if (board[new_y][i][-1] % 2 == 0) and (board[new_y][i][-1] != 0):
                            count += 1
                    if (count == 3)  or (count > 3  and (new_x != current_x or new_y != current_y)):
                        if move1 == True and board[current_y][current_x][-1] !=0:
                            board[current_y][current_x].pop()
                            board[new_y][new_x].append(selected-1)
                            move = True
                        
                    count = 0
                    #check 3 in a column
                    for i in range(1,5):
                        if (board[i][new_x][-1] % 2 == 0) and (board[i][new_x][-1] != 0):
                            count += 1
                    if (count == 3)  or (count > 3  and (new_x != current_x or new_y != current_y)):
                        if move1 == True and board[current_y][current_x][-1] !=0:
                            board[current_y][current_x].pop()
                            board[new_y][new_x].append(selected-1)
                            move = True
                    
                    #check 3 in a positive main diagonal
                    if (new_y == new_x):
                        count = 0
                        for i in range(1,5):
                            if (board[i][i][-1] %2 == 0) and (board[i][i][-1] != 0):
                                count += 1
                        if (count == 3)  or (count > 3  and (new_x != current_x or new_y != current_y)):
                            if move1 == True and board[current_y][current_x][-1] !=0:
                                board[current_y][current_x].pop()
                                board[new_y][new_x].append(selected-1)
                                move = True

                    #check 3 in a negative main diagonal
                    if (5 - new_y == new_x):
                        count = 0
                        for i in range(1,5):
                            if (board[i][5-i][-1] %2 == 0) and (board[i][5-i][-1] != 0):
                                count += 1
                        if (count == 3)  or (count > 3  and (new_x != current_x or new_y != current_y)):
                            if move1 == True and board[current_y][current_x][-1] !=0:
                                board[current_y][current_x].pop()
                                board[new_y][new_x].append(selected-1)
                                move = True      
                else:
                    if move1 == True and board[current_y][current_x][-1] !=0:
                        board[current_y][current_x].pop()
                        board[new_y][new_x].append(selected-1)
                        move = True
            else:
                if board[new_y][new_x][-1] < selected:
                    if (piece_on_board == True) and (board[new_y][new_x][-1] % 2 == 1):
                        count = 0
                        #check 3 in a row
                        for i in range(1,5):
                            if board[new_y][i][-1] % 2 == 1:
                                count += 1
                        if (count == 3)  or (count > 3  and (new_x != current_x or new_y != current_y)):
                            if move1 == True and board[current_y][current_x][-1] !=0:
                                board[current_y][current_x].pop()
                                board[new_y][new_x].append(selected)
                                move = True
                        
                        count = 0
                        #check 3 in a column
                        for i in range(1,5):
                            if board[i][new_x][-1] % 2 == 1:
                                count += 1
                        if (count == 3)  or (count > 3  and (new_x != current_x or new_y != current_y)):
                            if move1 == True and board[current_y][current_x][-1] !=0:
                                board[current_y][current_x].pop()
                                board[new_y][new_x].append(selected)
                                move = True
                        
                        #check 3 in a positive main diagonal
                        if new_y == new_x:
                            count = 0
                            for i in range(1,5):
                                if board[i][i][-1] % 2 == 1:
                                    count += 1
                            if (count == 3)  or (count > 3  and (new_x != current_x or new_y != current_y)):
                                if move1 == True and board[current_y][current_x][-1] !=0:
                                    board[current_y][current_x].pop()
                                    board[new_y][new_x].append(selected)
                                    move = True
                        
                        #check 3 in a negative main diagonal
                        if (5 - new_y == new_x):
                            count = 0
                            for i in range(1,5):
                                if board[i][5-i][-1] % 2 == 1:
                                    count += 1
                            if (count == 3)  or (count > 3  and (new_x != current_x or new_y != current_y)):
                                if move1 == True and board[current_y][current_x][-1] !=0:
                                    board[current_y][current_x].pop()
                                    board[new_y][new_x].append(selected)
                                    move = True
                    else:
                        if move1 == True and board[current_y][current_x][-1] !=0:
                            board[current_y][current_x].pop()
                            board[new_y][new_x].append(selected)
                            move = True
    return move










 # Function to check if a player has won
def winningPlayer(board):
                             #check 3 in a row
                                #global wins
                                global v
                                v=0
                                for i in range(1,5):
                                    count=0
                                    for j in range(1,5):
                                       
                                        if board[i][j][-1]%2==0 and board[i][j][-1] !=0:
                                           count=count+1
                                    if count>3:
                                         #wins="White"
                                         v=1
                                for i in range(1,5):
                                    count=0
                                    for j in range(1,5):
                                     if board[j][i][-1]%2==0 and board[j][i][-1] !=0:
                                        count=count+1
                                    if count>3:
                                        #wins="White"
                                        v=1
                                    
                                #check 3 in a positive main diagonal
                               
                                count=0
                                for i in range(1,5):
                                        if board[i][i][-1]%2==0 and board[i][i][-1] !=0:
                                            count=count+1
                                if count>3:
                                        #wins="White"
                                        v=1
                                        
                                #check 3 in a negative main diagonal
                                
                                count=0
                                for i in range(1,5):
                                        if board[i][5-i][-1]%2==0 and board[i][5-i][-1] !=0:
                                            count=count+1
                                if count>3:
                                        #wins="White"
                                        v=1


                                 #check 3 in a row
                                
                                for i in range(1,5):
                                    count=0
                                    for j in range(1,5):
                                        if board[j][i][-1]%2==1 :
                                           count=count+1
                                    if count>3:
                                        #wins="Black"
                                        v=-1
                                    
                                
                                for i in range(1,5):
                                    count=0
                                    for j in range(1,5):
                                     if board[i][j][-1]%2==1:
                                        count=count+1
                                    if count>3:
                                        #wins="Black"
                                        v=-1
                                    
                                #check 3 in a positive main diagonal
                               
                                count=0
                                for i in range(1,5):
                                        if board[i][i][-1]%2==1:
                                            count=count+1
                                if count>3:
                                        #wins="Black"
                                        v=-1
                                        
                                #check 3 in a negative main diagonal
                                
                                count=0
                                for i in range(1,5):
                                        if board[i][5-i][-1]%2==1:
                                            count=count+1
                                if count>3:
                                        #wins="Black"
                                        v=-1


                                return v

#*********************************************************************************************************************
                        
def evaluate(board):
    if winningPlayer(board)==1:
        return 1
    elif winningPlayer(board)==-1:
        return -1
    else:
        return 0


# Heuristic function for the AI
def heuristic(board):
    return evaluate(board)








def availablePieces(board, isWhite,Pieces):
    if isWhite:
        for x in range(1, 4):
            if board[0][x][-1] in (2, 4, 6, 8):
                Pieces.append([board[0][x][-1], 0,x])

        for i in range(1, 5):
          for j in range(1, 5):
              if board[i][j][-1] in (2, 4, 6, 8):
                 Pieces.append([board[i][j][-1], i,j])
                  

    else:
        for x in range(1, 4):
            if board[x][0][-1] in (1,3,5,7):
                Pieces.append([board[x][0][-1], x,0])
        for i in range(1, 5):
            for j in range(1, 5):
                if board[i][j][-1] in (1,3,5,7):
                    Pieces.append([board[i][j][-1], i,j])
                    

            
              
                  
def UndoMove(board, piece, old_x, old_y, current_x, current_y):
    if(board[current_x][current_y][-1]!=0):
        board[current_x][current_y].pop()

        board[old_x][old_y].append(piece)



def minimax(board, depth, is_maximizing , alpha, beta):
    result=heuristic(board)
    

    if depth == 0 or result==1 or result == -1  :
        return [result]
    if is_maximizing:
        prune=False
        final_score = -10
        final_i, final_j, piece, current_i, current_j = None, None, None, None, None
        whitePieces=[]
        availablePieces(board, True,whitePieces)
        for k in range(0, len(whitePieces)):
            if prune == True:
                break
            for i in range(1, 5):
                if prune == True:
                    break
                for j in range(1, 5):
                    valid = MakeMove(board, whitePieces[k][0], whitePieces[k][2], whitePieces[k][1], j, i)
                    if valid:
                       
                        
                        score = minimax(board, depth-1, False,alpha,beta)[0]
                        # print(score)
                        UndoMove(board, whitePieces[k][0], whitePieces[k][1], whitePieces[k][2], i, j)
                        if score > final_score:
                            final_score = score
                            
                            alpha = max(alpha, final_score)
                            final_i = i
                            final_j = j
                            piece = whitePieces[k][0]
                            current_i = whitePieces[k][1]
                            current_j = whitePieces[k][2]
                            if  alpha >= beta: 
                                prune=True
                                break
                

    else:
        prune =False
        final_score = 10
        final_i, final_j, piece, current_i, current_j = None, None, None, None, None
        blackPieces=[]
        availablePieces(board, False,blackPieces)
        for k in range(0, len(blackPieces)):
            if prune == True:
                break
            for i in range(1, 5):
                if prune == True:
                    break
                for j in range(1, 5):
                    valid= MakeMove(board,blackPieces[k][0], blackPieces[k][2], blackPieces[k][1], j, i)
                    if valid:
                        
                        score = minimax(board, depth-1, True,alpha,beta)[0]
                        # print(score)
                        UndoMove(board, blackPieces[k][0], blackPieces[k][1], blackPieces[k][2], i, j)
                        if score < final_score:
                            final_score = score
                            beta = min(beta,final_score)
                            final_i = i
                            final_j = j
                            piece = blackPieces[k][0]
                            current_i = blackPieces[k][1]
                            current_j = blackPieces[k][2]
                            if beta <= alpha:
                                prune = True
                                break

    # if first_time:
    #     board[final_i][final_j] = 'O'

    return [final_score,  piece, final_i, final_j,current_i,current_j]



# board=[[[0], [0, 2, 4, 6], [0, 2, 4, 6], [0, 2, 4, 6], [0]],
#  [[0, 1, 3, 5], [0, 8], [0, 8], [0,8], [0]],
#  [[0, 1, 3, 5], [0, 7], [0, 7], [0,7], [0]],
#  [[0, 1, 3, 5], [0], [0], [0], [0]],
#  [[0], [0], [0], [0], [0]]]
# board =[[[0], [0, 2, 4, 6, 8], [0, 2, 4, 6], [0, 2, 4, 6], [0]],
#  [[0, 1, 3, 5], [0, 7], [0], [0, 8], [0]],
#  [[0, 1, 3, 5, 7], [0], [0], [0], [0]],
#  [[0, 1, 3, 5, 7], [0], [0], [0], [0]],
#  [[0], [0], [0], [0], [0]]]
# minmax_output=minimax(board,4,True,-10000,10000)
# print(board)
# print( minmax_output)
