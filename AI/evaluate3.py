def check_for_3_for_whight(board):
    for i in range(1,5):
        count=0
        for j in range(1,5):
            if board[i][j][-1]%2==0 and board[i][j][-1] !=0:
                count=count+1
        if count==3:
            return True
            
    for i in range(1,5):
        count=0
        for j in range(1,5):
            if board[j][i][-1]%2==0 and board[j][i][-1] !=0:
                count=count+1
        if count==3:
            return True      
    for i in range(1,5):
        count=0
        for j in range(1,5):
            if board[i][i][-1]%2==0 and board[i][i][-1] !=0:
                count=count+1
        if count==3:
            return True
    for i in range(1,5):
        count=0
        for j in range(1,5):
            if board[i][5-i][-1]%2==0 and board[i][5-1][-1] !=0:
                count=count+1
        if count==3:
            return True
        
    return False
#***********************************************
def check_for_2_for_whight(board):
    for i in range(1,5):
        count=0
        for j in range(1,5):
            if board[i][j][-1]%2==0 and board[i][j][-1] !=0:
                count=count+1
        if count==2:
            return True
            
    for i in range(1,5):
        count=0
        for j in range(1,5):
            if board[j][i][-1]%2==0 and board[j][i][-1] !=0:
                count=count+1
        if count==2:
            return True      
    for i in range(1,5):
        count=0
        for j in range(1,5):
            if board[i][i][-1]%2==0 and board[i][i][-1] !=0:
                count=count+1
        if count==2:
            return True
    for i in range(1,5):
        count=0
        for j in range(1,5):
            if board[i][5-i][-1]%2==0 and board[i][5-1][-1] !=0:
                count=count+1
        if count==2:
            return True
        
    return False
#****************************************************
def check_for_1_for_whight(board):
    for i in range(1,5):
        count=0
        for j in range(1,5):
            if board[i][j][-1]%2==0 and board[i][j][-1] !=0:
                count=count+1
        if count==1:
            return True
            
    for i in range(1,5):
        count=0
        for j in range(1,5):
            if board[j][i][-1]%2==0 and board[j][i][-1] !=0:
                count=count+1
        if count==1:
            return True      
    for i in range(1,5):
        count=0
        for j in range(1,5):
            if board[i][i][-1]%2==0 and board[i][i][-1] !=0:
                count=count+1
        if count==1:
            return True
    for i in range(1,5):
        count=0
        for j in range(1,5):
            if board[i][5-i][-1]%2==0 and board[i][5-1][-1] !=0:
                count=count+1
        if count==1:
            return True
        
    return False
#***********************************************************
def check_for_4_for_whight(board):
    for i in range(1,5):
        count=0
        for j in range(1,5):
            if board[i][j][-1]%2==0 and board[i][j][-1] !=0:
                count=count+1
        if count==4:
            return True
            
    for i in range(1,5):
        count=0
        for j in range(1,5):
            if board[j][i][-1]%2==0 and board[j][i][-1] !=0:
                count=count+1
        if count==4:
            return True      
    for i in range(1,5):
        count=0
        for j in range(1,5):
            if board[i][i][-1]%2==0 and board[i][i][-1] !=0:
                count=count+1
        if count==4:
            return True
    for i in range(1,5):
        count=0
        for j in range(1,5):
            if board[i][5-i][-1]%2==0 and board[i][5-1][-1] !=0:
                count=count+1
        if count==4:
            return True
        
    return False
#***********************************************************
def check_for_3_for_black(board):
    for i in range(1,5):
        count=0
        for j in range(1,5):
            if board[i][j][-1]%2==1:
                count=count+1
        if count==3:
            return True
            
    for i in range(1,5):
        count=0
        for j in range(1,5):
            if board[j][i][-1]%2==1:
                count=count+1
        if count==3:
            return True      
    for i in range(1,5):
        count=0
        for j in range(1,5):
            if board[i][i][-1]%2==1:
                count=count+1
        if count==3:
            return True
    for i in range(1,5):
        count=0
        for j in range(1,5):
            if board[i][5-i][-1]%2==1:
                count=count+1
        if count==3:
            return True
        
    return False
#************************************************************
def check_for_4_for_black(board):
    for i in range(1,5):
        count=0
        for j in range(1,5):
            if board[i][j][-1]%2==1:
                count=count+1
        if count==4:
            return True
            
    for i in range(1,5):
        count=0
        for j in range(1,5):
            if board[j][i][-1]%2==1:
                count=count+1
        if count==4:
            return True      
    for i in range(1,5):
        count=0
        for j in range(1,5):
            if board[i][i][-1]%2==1:
                count=count+1
        if count==4:
            return True
    for i in range(1,5):
        count=0
        for j in range(1,5):
            if board[i][5-i][-1]%2==1:
                count=count+1
        if count==4:
            return True
        
    return False
#**************************************************************
def check_for_2_for_black(board):
    for i in range(1,5):
        count=0
        for j in range(1,5):
            if board[i][j][-1]%2==1:
                count=count+1
        if count==2:
            return True
            
    for i in range(1,5):
        count=0
        for j in range(1,5):
            if board[j][i][-1]%2==1:
                count=count+1
        if count==2:
            return True      
    for i in range(1,5):
        count=0
        for j in range(1,5):
            if board[i][i][-1]%2==1:
                count=count+1
        if count==2:
            return True
    for i in range(1,5):
        count=0
        for j in range(1,5):
            if board[i][5-i][-1]%2==1:
                count=count+1
        if count==2:
            return True
        
    return False
#**************************************************************
def check_for_1_for_black(board):
    for i in range(1,5):
        count=0
        for j in range(1,5):
            if board[i][j][-1]%2==1:
                count=count+1
        if count==1:
            return True
            
    for i in range(1,5):
        count=0
        for j in range(1,5):
            if board[j][i][-1]%2==1:
                count=count+1
        if count==1:
            return True      
    for i in range(1,5):
        count=0
        for j in range(1,5):
            if board[i][i][-1]%2==1:
                count=count+1
        if count==1:
            return True
    for i in range(1,5):
        count=0
        for j in range(1,5):
            if board[i][5-i][-1]%2==1:
                count=count+1
        if count==1:
            return True
        
    return False
#*********************************************************
def evaluate(board):
    
        if check_for_4_for_whight(board):
            return 1000
        elif check_for_4_for_black(board):
            return -1000
        elif check_for_3_for_whight(board):
            return 100
        elif check_for_3_for_black(board):
            return -100
        elif check_for_2_for_whight(board):
            return 10
        elif check_for_2_for_black(board):
            return -10
        elif check_for_1_for_whight(board):
            return 1
        elif check_for_1_for_black(board):
            return-1
        else:
            return 0
        
        









































    

            
    
