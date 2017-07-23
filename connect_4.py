# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 18:42:21 2017

@author: HP-HP
"""

import numpy as np
import scipy as sc
import pandas as pd
import seaborn as sns
#import matplotlib.pyplot as plt
import matplotlib.pylab as plt
import time
from IPython import display
%matplotlib inline

empty_board_dict = { 0 : [ [0,0] , [0,0] , [0,0] , [0,0] , [0,0] , [0,0] ],
                     1 : [ [0,0] , [0,0] , [0,0] , [0,0] , [0,0] , [0,0] ],
                     2 : [ [0,0] , [0,0] , [0,0] , [0,0] , [0,0] , [0,0] ],
                     3 : [ [0,0] , [0,0] , [0,0] , [0,0] , [0,0] , [0,0] ],
                     4 : [ [0,0] , [0,0] , [0,0] , [0,0] , [0,0] , [0,0] ],
                     5 : [ [0,0] , [0,0] , [0,0] , [0,0] , [0,0] , [0,0] ],
                     6 : [ [0,0] , [0,0] , [0,0] , [0,0] , [0,0] , [0,0] ] }
    
empty_board = pd.DataFrame(empty_board_dict , index = [0,1,2,3,4,5])



example1_board_dict = { 0 : [ [0,1] , [1,0] , [0,0] , [0,0] , [0,0] , [0,0] ] ,
                     1 : [ [0,1] , [1,0] , [0,0] , [0,0] , [0,0] , [0,0] ],
                     2 : [ [0,0] , [0,1] , [0,0] , [0,0] , [0,0] , [0,0] ],
                     3 : [ [0,0] , [0,0] , [0,1] , [0,0] , [0,0] , [0,0] ],
                     4 : [ [0,0] , [0,0] , [0,0] , [0,1] , [0,0] , [0,0] ],
                     5 : [ [0,0] , [0,0] , [0,0] , [0,0] , [0,0] , [0,0] ],
                     6 : [ [0,0] , [0,0] , [0,0] , [0,0] , [0,0] , [0,0] ] }

example1_board = pd.DataFrame(example1_board_dict , index = [0,1,2,3,4,5])







dummy = pd.DataFrame({
                      0 : [ [1,1] , [1,0] , [0,0] , [0,0] , [0,0] , [0,0] ] ,
                     1 : [ [1,1] , [1,0] , [0,0] , [0,0] , [0,0] , [0,0] ],
                     2 : [ [1,1] , [0,1] , [0,0] , [0,0] , [0,0] , [0,0] ],
                     3 : [ [1,1] , [0,0] , [0,1] , [0,0] , [0,0] , [0,0] ],
                     4 : [ [1,1] , [0,0] , [0,0] , [0,1] , [0,0] , [0,0] ],
                     5 : [ [1,1] , [0,0] , [0,0] , [0,0] , [0,0] , [0,0] ],
                     6 : [ [1,1] , [0,0] , [0,0] , [0,0] , [0,0] , [0,0] ] }
                        , index = [0,1,2,3,4,5])


dummy_hor = pd.DataFrame({
                      0 : [ [0,0] , [1,0] , [0,0] , [0,0] , [0,0] , [0,0] ] ,
                     1 : [ [0,0] , [1,0] , [0,0] , [0,0] , [0,0] , [0,0] ],
                     2 : [ [0,1] , [0,1] , [0,1] , [0,0] , [0,1] , [0,0] ],
                     3 : [ [0,0] , [0,0] , [0,1] , [0,0] , [0,1] , [0,0] ],
                     4 : [ [1,0] , [0,0] , [0,0] , [0,1] , [0,1] , [0,0] ],
                     5 : [ [0,1] , [0,1] , [0,1] , [0,0] , [0,1] , [0,0] ],
                     6 : [ [1,1] , [0,0] , [0,0] , [0,0] , [0,0] , [0,0] ] }
                        , index = [0,1,2,3,4,5])

dummy_ver = pd.DataFrame({
                      0 : [ [0,0] , [1,0] , [0,0] , [0,0] , [0,0] , [0,0] ] ,
                     1 : [ [0,0] , [1,0] , [0,0] , [0,0] , [0,0] , [0,0] ],
                     2 : [ [0,0] , [0,1] , [0,1] , [0,1] , [0,1] , [0,0] ],
                     3 : [ [0,0] , [0,0] , [0,1] , [0,0] , [0,0] , [0,0] ],
                     4 : [ [1,0] , [0,0] , [0,0] , [0,1] , [0,1] , [0,0] ],
                     5 : [ [0,1] , [0,1] , [0,1] , [0,0] , [0,1] , [0,0] ],
                     6 : [ [1,0] , [0,0] , [0,0] , [0,0] , [0,0] , [0,0] ] }
                        , index = [0,1,2,3,4,5])



dummy_dia2 = pd.DataFrame({
                      0 : [ [0,0] , [1,0] , [0,0] , [0,0] , [0,0] , [0,0] ] ,
                     1 : [ [0,0] , [1,0] , [0,0] , [0,0] , [0,0] , [0,0] ],
                     2 : [ [0,0] , [0,1] , [0,0] , [0,1] , [0,1] , [0,0] ],
                     3 : [ [0,0] , [0,0] , [0,1] , [0,1] , [0,0] , [0,0] ],
                     4 : [ [1,0] , [0,0] , [0,1] , [0,1] , [0,1] , [0,0] ],
                     5 : [ [0,1] , [0,1] , [0,1] , [0,0] , [0,1] , [0,0] ],
                     6 : [ [1,0] , [0,0] , [0,0] , [0,0] , [0,0] , [0,0] ] }
                        , index = [0,1,2,3,4,5])


dummy_dia1 = pd.DataFrame({
                      0 : [ [0,0] , [1,0] , [1,0] , [0,0] , [0,0] , [0,0] ] ,
                     1 : [ [0,0] , [1,0] , [0,0] , [1,0] , [0,0] , [0,1] ],
                     2 : [ [0,0] , [0,1] , [0,0] , [0,1] , [1,0] , [0,0] ],
                     3 : [ [0,0] , [0,0] , [0,0] , [0,0] , [0,0] , [1,0] ],
                     4 : [ [1,0] , [0,0] , [0,1] , [0,1] , [0,1] , [0,0] ],
                     5 : [ [0,1] , [0,0] , [0,1] , [0,0] , [0,0] , [0,0] ],
                     6 : [ [1,0] , [0,0] , [0,0] , [0,0] , [0,0] , [0,0] ] }
                        , index = [0,1,2,3,4,5])

dummy_no = pd.DataFrame({
                      0 : [ [1,0] , [0,0] , [1,0] , [0,1] , [0,0] , [0,0] ] ,
                     1 : [ [0,1] , [0,0] , [0,0] , [1,0] , [0,0] , [0,1] ],
                     2 : [ [1,0] , [0,0] , [0,0] , [0,1] , [1,0] , [0,0] ],
                     3 : [ [0,1] , [0,0] , [0,0] , [1,0] , [0,0] , [1,0] ],
                     4 : [ [1,0] , [0,0] , [0,1] , [0,1] , [0,1] , [0,0] ],
                     5 : [ [0,1] , [0,0] , [0,1] , [1,0] , [0,0] , [1,0] ],
                     6 : [ [1,0] , [0,0] , [0,0] , [0,1] , [0,0] , [0,0] ] }
                        , index = [0,1,2,3,4,5])

# BOARD IS A 7 x 6 DATAFRAME
# TURN IS 0 OR 1, DEPENDING ON WHOS TURN IT IS
# POSITION IS AN INTEGER BETWEEN 0 AND 5



def pos_available(board, position):
    if position > 6 or position < 0:
        return False
    else:
        if board[position][0][0] + board[position][0][1]  > 0  :
            return False
    return True
        
        
print pos_available(dummy,1)
print pos_available(example1_board,0)
print pos_available(dummy_hor,5)
dummy_hor

def put_in_next(board, turn, position):
    if pos_available(board, position) == False:
        return 'column is full' 
    i = 5
    while board[position][i][0] + board[position][i][1]  > 0:
        i = i - 1
    board[position][i][turn] = 1

#put_in_next(empty_board,0,2)

def check_win(board, turn):
    for i in range(0,6):
        # check horizontal
        j = 0
        while j < 4:
            #print board[j][i][turn] ,board[j+1][i][turn] , board[j+2][i][turn] , board[j+3][i][turn] 
            if board[j][i][turn] + board[j+1][i][turn] + board[j+2][i][turn] + board[j+3][i][turn] == 4:
                return turn
            j = j + 1
    for j in range(0,7):
        #check vertical 
        i = 0
        while i < 3:
            #print board[j][i][turn] ,board[j][i+1][turn] , board[j][i+2][turn] , board[j][i+3][turn] 
            if board[j][i][turn] + board[j][i+1][turn] + board[j][i+2][turn] + board[j][i+3][turn] == 4:
                return turn
            i = i + 1
    for j in range(0,4):
        #check diagonal1
        i = 0
        while i < 3:
            if board[j][i][turn] + board[j+1][i+1][turn] + board[j+2][i+2][turn] + board[j+3][i+3][turn] == 4:
                return turn
            i = i + 1 
    for j in range(0,4):
        #check diagonal2
        i = 5
        while i > 2:
            #print board[j][i][turn] , board[j+1][i-1][turn] , board[j+2][i-2][turn] , board[j+3][i-3][turn]
            if board[j][i][turn] + board[j+1][i-1][turn] + board[j+2][i-2][turn] + board[j+3][i-3][turn] == 4:
                return turn
            i = i - 1 
    return 'No one won this round' 




plt.matshow(np.array([[ 0,1,2,0,0,0],
       [ 0,0,0,0,0,0],
       [ 0,0,0,0,0,0],
       [ 0,0,0,0,0,0],
       [ 0,0,0,0,0,0]]), cmap=plt.cm.bwr)

empty = np.array([[ 1,1,1,1,1,1,1],
       [ 1,1,1,1,1,1,1],
       [ 1,1,1,1,1,1,1],
       [ 1,1,1,1,1,1,1],
       [ 1,1,1,1,1,1,1],
       [ 1,1,1,1,1,1,1]])

    
type(example1_board)
example1_board[1][0]
    
def visualise_board(board):
    empty = np.array([ [ 1,1,1,1,1,1,1],
                       [ 1,1,1,1,1,1,1],
                       [ 1,1,1,1,1,1,1],
                       [ 1,1,1,1,1,1,1],
                       [ 1,1,1,1,1,1,1],
                       [ 1,1,1,1,1,1,1]])
    for i in range(0,7):
        for j in range(0,6):
            if board[i][j]== [0, 1]:
                empty[j,i] = 0
            if board[i][j] == [1,0]:
                empty[j,i] = 2
    return plt.matshow(empty, cmap=plt.cm.bwr)

i = 4
j=3
example1_board[i][j]== [0, 1]

empty[j,i]


visualise_board(example1_board)

#i , j = 5 , 0
   
#dummy_dia1[j][i][0] + dummy_dia1[j+1][i+1][0] + dummy_dia1[j+2][i+2][0] + dummy_dia1[j+3][i+3][0]
    
#check_win(empty_board, 0)
#check_win(dummy_hor, 1)
#check_win(dummy_dia1, 0)
#check_win(dummy_dia1, 1)
#check_win(dummy_dia2, 0)
#check_win(dummy_dia2, 1)
#check_win(dummy_no, 1)
#dummy_ver
    
def input_connect4(board , turn, position):
    k = 0
    for i in range(7):
        if pos_available(board, i) == False:
            k = k + 1
    if k == 7:
        print 'board is full' 
        return 1 
   # CHECK IF POSITION IS AVAILABLE, OTHERWISE RETURN SAME BOARD AND PLAYER AND TURN 
    if pos_available(board, position) == False:
        print "Position not available"
        return 0 
    # PUT IN NEXT TOKEN 
    put_in_next(board, turn, position)
    # CHECK IF SOMEONE HAS WON
    if check_win(board, turn) == 'No one won this round':
        #turn = (turn+1) % 2
        return 0
    else:
        print 'player ' + str(turn) + ' won' 
        return 1

            
input_connect4(dummy , 1, 4)
    
empty_board_dict = { 0 : [ [0,0] , [0,0] , [0,0] , [0,0] , [0,0] , [0,0] ],
                     1 : [ [0,0] , [0,0] , [0,0] , [0,0] , [0,0] , [0,0] ],
                     2 : [ [0,0] , [0,0] , [0,0] , [0,0] , [0,0] , [0,0] ],
                     3 : [ [0,0] , [0,0] , [0,0] , [0,0] , [0,0] , [0,0] ],
                     4 : [ [0,0] , [0,0] , [0,0] , [0,0] , [0,0] , [0,0] ],
                     5 : [ [0,0] , [0,0] , [0,0] , [0,0] , [0,0] , [0,0] ],
                     6 : [ [0,0] , [0,0] , [0,0] , [0,0] , [0,0] , [0,0] ] }
    
empty_board = pd.DataFrame(empty_board_dict , index = [0,1,2,3,4,5])    


# in this game player 0 wins 
visualise_board(empty_board)
input_connect4(empty_board , 0, 3)  
visualise_board(empty_board)
input_connect4(empty_board , 1, 3)  
visualise_board(empty_board)
input_connect4(empty_board , 0, 4)  
visualise_board(empty_board)
input_connect4(empty_board , 1, 4)  
visualise_board(empty_board)
input_connect4(empty_board , 0, 5)  
visualise_board(empty_board)
input_connect4(empty_board , 1, 2)  
visualise_board(empty_board)
input_connect4(empty_board , 0, 6) 
visualise_board(empty_board)
input_connect4(empty_board , 1, 2)  
visualise_board(empty_board)
input_connect4(empty_board , 0, 6) 
visualise_board(empty_board)

# everything on column 3
input_connect4(empty_board , 0, 3)  
input_connect4(empty_board , 1, 3)  
input_connect4(empty_board , 0, 3)  
input_connect4(empty_board , 1, 3)  
input_connect4(empty_board , 0, 3)  
input_connect4(empty_board , 1, 3)  
input_connect4(empty_board , 0, 3) 
input_connect4(empty_board , 1, 3)  
input_connect4(empty_board , 0, 3)   


input_connect4(dummy , 0, 3)  





print empty_board 
    
    

def human_vs_human():
    turn = 0
    #plt.ion()
    board = pd.DataFrame({ 0 : [ [0,0] , [0,0] , [0,0] , [0,0] , [0,0] , [0,0] ],
                                 1 : [ [0,0] , [0,0] , [0,0] , [0,0] , [0,0] , [0,0] ],
                                 2 : [ [0,0] , [0,0] , [0,0] , [0,0] , [0,0] , [0,0] ],
                                 3 : [ [0,0] , [0,0] , [0,0] , [0,0] , [0,0] , [0,0] ],
                                 4 : [ [0,0] , [0,0] , [0,0] , [0,0] , [0,0] , [0,0] ],
                                 5 : [ [0,0] , [0,0] , [0,0] , [0,0] , [0,0] , [0,0] ],
                                 6 : [ [0,0] , [0,0] , [0,0] , [0,0] , [0,0] , [0,0] ] } , index = [0,1,2,3,4,5]) 

    print board
    
    print "Player 0, where do you want to put it?" 
    position = input()

    while input_connect4(board , turn, position) != 1:
        if pos_available(board, position) == True:
            turn = (turn + 1)%2   
        # print the board
        print board 
        print "Player " + str(turn) + ", where do you want to put it?" 
        position = input()
        #input_connect4(board , turn, position)
    return board


 
human_vs_human()



def human_vs_pc():
    True


















   
    
    
    
    
    