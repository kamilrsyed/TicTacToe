from IPython.display import clear_output
import random

def display_board(board):
    clear_output()
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-----')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-----')
    print(board[1] + '|' + board[2] + '|' + board[3])

def player_input():
    choices = ['X', 'O']
    marker = input('Please choose your marker X or O: ')
    
    while marker not in choices:
        marker = input('Please choose your marker X or O: ')
    
    player_1_marker = marker
    player_2_marker = choices[0] if player_1_marker == choices[1] else choices[1]
    print(f'Player 1 has marker {player_1_marker} and Player 2 has marker {player_2_marker}.')
    return [player_1_marker, player_2_marker]

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    win_list = [mark, mark, mark]
    if board[1:4] == win_list or board[4:7] == win_list or board[7:] == win_list:   # Checks winning combinations horizontally 
        return True
    elif board[5] == mark:
        if (board[1] == mark and board[9] == mark) or (board[3] == mark and board[7] == mark) or (board[2] == mark and board[8] == mark):   # Checks winning combinations diagonally and middle vertical
            return True
    elif board[4] == mark:
        if (board[1] == mark and board[7] == mark):    # Checks winning combinations left vertical
            return True
    elif board[6] == mark:
        if (board[3] == mark and board[9] == mark):    # Checks winning combinations right vertical
            return True
    else:
        return False

def choose_first():     # Randomly picks first turn
    num = random.randint(1, 2)
    if num == 1:
        return 1
    else:
        return 2
    
def space_check(board, position):
    return board[position] != 'X' or board[position] != 'O'

def full_board_check(board):
    if ' ' in board:
        return False
    else:
        return True
    
def player_choice(board):
    next_pos = int(input('Choose your next position 1-9: '))
    if space_check(board, next_pos):
        return next_pos
    
def replay():
    play_again = input('Do you want to play again? Y/N')
    if play_again == 'Y':
        return True
    else:
        return False
    
def reset():
    board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    player_markers = player_input()
    first_turn = choose_first()
    print(f'Player {first_turn} turn')
    next_pos = player_choice(board)
    
    if first_turn == 1:
        place_marker(board, player_markers[0], next_pos)
        next_turn = 2
    else:
        place_marker(board, player_markers[1], next_pos)
        next_turn = 1
        
    return [board, player_markers, next_turn]

play = True
game_over = False

while play:
    reset_data = reset()
    board = reset_data[0]
    player_markers = reset_data[1]
    next_turn = reset_data[2]
    display_board(board)
    
    while play:
        next_pos = player_choice(board)
        
        if next_turn == 1:
            place_marker(board, player_markers[0], next_pos)
            next_turn = 2
            display_board(board)            
            if win_check(board, player_markers[0]):
                print('Player 1 won!')
                game_over = True
                
        elif next_turn == 2:
            place_marker(board, player_markers[1], next_pos)
            next_turn = 1
            display_board(board)            
            if win_check(board, player_markers[1]):
                print('Player 2 won!')
                game_over = True
                
        if full_board_check(board) or game_over:
            if replay():
                play = True
                game_over = False
                break
            else:
                play = False