from IPython.display import clear_output

def display_board(board):
    clear_output()
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-----')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-----')
    print(board[1]+'|'+board[2]+'|'+board[3])

test_board = [' ']*10
display_board(test_board)

def player_input():
    
    marker = ''
    
    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O: ').upper()
    
    if marker == 'X':
        
        return('X', 'O')
    else:
        return('O', 'X')
    
# player1_marker , player2_marker = player_input()    
    # player1 = marker
    
    # if player1 == 'X':
    #     player2 = 'O'
    # else:
    #     player2 = 'X'
        
    #     return (player1,player2)
# player_input()

def place_marker(board, marker, position):
    board[position] = marker
    
    
def win_check(board, mark):
    return ((board[1] == board[2] == board[3] == mark) or
    (board[4] == board[5] == board[6] == mark) or 
    (board[7] == board[8] == board[9] == mark) or
    (board[7] == board[4] == board[1] == mark) or
    (board[8] == board[5] == board[2] == mark) or
    (board[9] == board[6] == board[3] == mark) or
    (board[7] == board[5] == board[3] == mark) or
    (board[9] == board[5] == board[1] == mark))
    
import random

def choose_first():
    flip = random.randint(0,1)
    
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):
    
    return(board[position] == ' ')

def full_board_check(board):
    
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    
    position = 0
    
    while position not in range(1,10) or not space_check(board, position):
        position = int(input('Chooce a position: (1-9): '))
    return position

def replay():
    choice = input('Play again? Enter Yes or No: ')
    
    return choice == 'Yes'

print('Welcome to Tic Tac Toe!')

while True:
    
    #GAME SETUP
    game_board = [' ']*10
    
    player1_marker , player2_marker = player_input()
    
    turn = choose_first()
    print(turn + ' will be the first to play')
    
    play_game = input('Ready to begin? y or n: ')
    
    if play_game == 'y':
        game_start = True
    else:
        game_start == False
        
    ##GAME START
    while game_start:
        
        if turn == 'Player 1':
           display_board(game_board)
           position = player_choice(game_board)
           place_marker(game_board, player1_marker, position)
           
           if win_check(game_board, player1_marker):
               display_board(game_board)
               print('PLAYER 1 IS THE WINNER!')
               game_start = False
           else:
               if full_board_check(game_board):
                   display_board(game_board)
                   print('TIE GAME!')
                   game_start = False
               else:
                   turn = 'Player 2'
        else:
            display_board(game_board)
            position = player_choice(game_board)
            place_marker(game_board, player2_marker, position)
            
            if win_check(game_board, player2_marker):
               display_board(game_board)
               print('PLAYER 2 IS THE WINNER!')
               game_start = False
            else:
                if full_board_check(game_board):
                   display_board(game_board)
                   print('TIE GAME!')
                   game_start = False
                else:
                   turn = 'Player 1'
    if not replay():
        break