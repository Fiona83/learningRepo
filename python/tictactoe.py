"""
This original code is downloaded from jackfrued's Python-100-days
https://github.com/jackfrued/Python-100-Days
The original game has several problems:
1. the input must be in upper case, otherwise will cause a trackback
2. the game won't stop until 9 blanks are filled, even one player wins,
the game won't stop

my modifications:
1. add upper() to cast the input into upper cause
2. define a is_win function to test if someone has won. If so, end the
game.
3. add the input done to terminate the game

date: 2022-09-12
author: Yerong Chen
"""
import os

def print_board(board):
    print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
    print('-+-+-')
    print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
    print('-+-+-')
    print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])

def is_won(turn, board):
    return (board["TL"] == turn and board["TM"] == turn and board["TR"] == turn) \
    or (board["ML"] == turn and board["MM"] == turn and board["MR"] == turn) \
    or (board["BL"] == turn and board["BM"] == turn and board["BR"] == turn) \
    or (board["TL"] == turn and board["ML"] == turn and board["BL"] == turn) \
    or (board["TM"] == turn and board["MM"] == turn and board["BM"] == turn) \
    or (board["TR"] == turn and board["MR"] == turn and board["BR"] == turn) \
    or (board["TL"] == turn and board["MM"] == turn and board["BR"] == turn) \
    or (board["TR"] == turn and board["MM"] == turn and board["BL"] == turn)



def main():
    init_board = {
        'TL': ' ', 'TM': ' ', 'TR': ' ',
        'ML': ' ', 'MM': ' ', 'MR': ' ',
        'BL': ' ', 'BM': ' ', 'BR': ' '
    }
    begin = True
    while begin:
        curr_board = init_board.copy()
        begin = False
        turn = 'x'
        counter = 0
        os.system('clear')
        print_board(curr_board)
        while counter < 9:
            move = input('轮到%s走棋, 请输入位置: ' % turn)
            # add this to terminate the game
            if move == "done":
                print("Game is terminated!")
                begin = False
                break
            # add this line sothat the user can input lower case value
            move = move.upper()
            if move not in init_board:
                print("Invalid position! Please try again.")
                continue


            if curr_board[move] == ' ':
                counter += 1
                curr_board[move] = turn
                os.system('clear')
                print_board(curr_board)
                # here should check if someone has won
                if is_won(turn, curr_board):
                    begin = False
                    print("%s has won! Game over!" % turn)
                    break

                if turn == 'x':
                    turn = 'o'
                else:
                    turn = 'x'
            else:
                print("Position is already occupied. Try again.")
                continue
            #os.system('clear')
            #print_board(curr_board)
        choice = input('再玩一局?(yes|no)')
        begin = choice == 'yes'


if __name__ == '__main__':
    main()
