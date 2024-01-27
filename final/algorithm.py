def evaluate3(board,player):
    # declare variables to store sum for the black player (minmizer) at each direction
    row_matrix_sum_black=[0]*4
    col_matrix_sum_black=[0]*4
    diagonal_matrix_sum_black=[0]*2

    # declare variables to store sum for the white player (maximizer)at each direction
    row_matrix_sum_white=[0]*4
    col_matrix_sum_white=[0]*4
    diagonal_matrix_sum_white=[0]*2
    #map input as if player white its value=-1 ,if black value=1
    player=int(player)*-2+1
    for row in range(1,5):
        for col in range(1,5):
            #check for each board cell the piece is black or white
            is_black=int((board[row][col][-1]%2==1) and (board[row][col][-1]!=0))
            is_white=int((board[row][col][-1]%2==0) and (board[row][col][-1]!=0))
            #count the number of white pieces at each row and store each sum at row_matrix_sum_white
            #and the number of black pieces at each row and store each sum at row_matrix_sum_black
            row_matrix_sum_black[row-1]+=is_black
            row_matrix_sum_white[row-1]+=is_white
            #count the number of white pieces at each col and store each sum at row_matrix_sum_white
            #and the number of black pieces at each col and store each sum at row_matrix_sum_black
            col_matrix_sum_black[col-1]+=is_black
            col_matrix_sum_white[col-1]+=is_white
            #count the number of white pieces at each postive diagonal and store each sum at diagonal_matrix_sum_white
            #count the number of white pieces at each negative diagonal and store each sum at diagonal_matrix_sum_white
            if(row==col):
                diagonal_matrix_sum_black[0]+=is_black
                diagonal_matrix_sum_white[0]+=is_white
            elif(row+col==5):
                diagonal_matrix_sum_black[1]+=is_black
                diagonal_matrix_sum_white[1]+=is_white
    #get the max number of pieces            
    whiht_max=max(max(row_matrix_sum_white),max(col_matrix_sum_white),max(diagonal_matrix_sum_white))*250*-player
    black_max=max(max(row_matrix_sum_black),max(col_matrix_sum_black),max(diagonal_matrix_sum_black))*250*player
    return max(whiht_max,black_max,key=abs)*-player
                
# Heuristic function for AI
def heuristic(board,player):
    return evaluate3(board,player)






def UndoMove(board, piece, old_x, old_y, current_x, current_y):
    if(board[current_x][current_y][-1]!=0):
        board[current_x][current_y].pop()

        board[old_x][old_y].append(piece)



def minimax2(board, depth, is_maximizing , alpha, beta):
    result=heuristic2(board,is_maximizing)
    if depth == 0 or result==1000 or result == -1000  :
        return [result]
    if is_maximizing:
        prune=False
        final_score = -3000
        final_i, final_j, piece, current_i, current_j = None, None, None, None, None
        whitePieces=[]
        availablePieces(board, True,whitePieces)
        random.shuffle(whitePieces)
        for k in range(0, len(whitePieces)):
            if prune == True:
                break
            for i in range(1, 5):
                if prune == True:
                    break
                for j in range(1, 5):
                    valid = MakeMove(board, whitePieces[k][0], whitePieces[k][2], whitePieces[k][1], j, i)
                    if valid:
                        board[i][j].append(whitePieces[k][0])
                        board[whitePieces[k][1]][whitePieces[k][2]].pop()
                        score = minimax(board, depth-1, False,alpha,beta)[0]
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
        final_score = 3000
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
                        board[i][j].append(blackPieces[k][0])
                        board[blackPieces[k][1]][blackPieces[k][2]].pop()
                        score = minimax(board, depth-1, True,alpha,beta)[0]
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

 

    return [final_score,  piece, final_i, final_j,current_i,current_j]


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
        random.shuffle(whitePieces)
        for k in range(0, len(whitePieces)):
            if prune == True:
                break
            for i in range(1, 5):
                if prune == True:
                    break
                for j in range(1, 5):
                    valid = MakeMove(board, whitePieces[k][0], whitePieces[k][2], whitePieces[k][1], j, i)
                    if valid:
                        board[i][j].append(whitePieces[k][0])
                        board[whitePieces[k][1]][whitePieces[k][2]].pop()
                       
                        
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
                        board[i][j].append(blackPieces[k][0])
                        board[blackPieces[k][1]][blackPieces[k][2]].pop()
                        
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

 

    return [final_score,  piece, final_i, final_j,current_i,current_j]











