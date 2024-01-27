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




