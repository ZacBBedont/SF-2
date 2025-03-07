#Zaccaria Broomhall Bedont 2438041

import random
import sys

def displayBoard(board_lst):
    n = len(board_lst)

    labels = []
    for i in range(n):
        for j in range(n):
            labels.append(board_lst[i][j])

    draw_board = ''
    horizontal_div = ('+' + '------')*n + '+'
    vertical_div = '|' + ' '*6
    vertical_label = '|' + ' '*2 + '{}' + ' '*2
    
    for i in range(n):
        draw_board = draw_board + horizontal_div +'\n'+\
                    vertical_div*n + '|\n' + \
                    vertical_label*n + '|\n'+\
                    vertical_div*n + '|\n'
    draw_board += horizontal_div
    print(draw_board.format(*labels))

def tileLabels(n):
    labels =[]
    for tile in range(n**2-1):
        labels.append(str(tile+1))
    labels.append("  ")
    return labels

def getNewPuzzle(n):
    board = []
    tile_labels = tileLabels(n)
    for tile in range(n**2):
        if len(tile_labels[tile]) == 1:
            tile_labels[tile] = tile_labels[tile] + " "
    random.shuffle(tile_labels)
    for _ in range(n):
        board += [tile_labels[:n]]
        tile_labels = tile_labels[n:]
    return board

def findEmptyTile(board):
    found = False
    row_number = 0
    column_number = 0
    while not found:
        if board[row_number][column_number] == "  ":
            location = (row_number,column_number)
            found = True
        column_number += 1
        if column_number == len(board[row_number]):
            column_number = 0
            row_number += 1
    return location

def nextMove(board):
    moves = ["W","A","S","D"]
    empty_tile = findEmptyTile(board)
    displayBoard(board)
    valid = False

    if empty_tile[0] == 0:
        moves[2] = " "
    elif empty_tile[0] == len(board)-1:
        moves[0] = " "
    if empty_tile[1] == 0:
        moves[3] = " "
    elif empty_tile[1] == len(board)-1:
        moves[1] = " "
    
    while not valid:
        print(f"\t\t\t  ({moves[0]})\nEnter WASD (or QUIT): ({moves[1]}) ({moves[2]}) ({moves[3]})")
        user_input = input("> ")
        if user_input.lower() == "quit":
            sys.exit()
        elif user_input in moves:
            return user_input
        print("please input a valid move")

def makeMove(board,move):
    empty_tile = findEmptyTile(board)
    if move == "D":
        board[empty_tile[0]][empty_tile[1]], board[empty_tile[0]][empty_tile[1]-1] = board[empty_tile[0]][empty_tile[1]-1], board[empty_tile[0]][empty_tile[1]]
    elif move == "A":
        board[empty_tile[0]][empty_tile[1]], board[empty_tile[0]][empty_tile[1]+1] = board[empty_tile[0]][empty_tile[1]+1], board[empty_tile[0]][empty_tile[1]]
    elif move == "S":
        board[empty_tile[0]][empty_tile[1]], board[empty_tile[0]-1][empty_tile[1]] = board[empty_tile[0]-1][empty_tile[1]], board[empty_tile[0]][empty_tile[1]]
    else:
        board[empty_tile[0]][empty_tile[1]], board[empty_tile[0]+1][empty_tile[1]] = board[empty_tile[0]+1][empty_tile[1]], board[empty_tile[0]][empty_tile[1]]

def isOver(board,moves,n):
    empty_row = []
    board_list = []
    if (moves > 31) and (n == 3):
        return True
    elif (moves > 80) and (n == 4):
        return True
    for row in board:
        if "  " not in row:
            if sorted(row) != row:
                return False
            else:
                board_list += row
        elif "  " in row:
            for element in row:
                if element != "  ":
                    empty_row.append(element)
            board_list += empty_row
    print(board_list)
    if sorted(board_list) != board_list:
        return False
    return True

print("Welcome! you will create a board which you need to sort numerically by swapping numbers with the blank space in the board.\n controls are as follows when prompted: W to make a block move upwards, S to make a block move downwards, D to make the block move to the right and A to make the block move to the left.")
n = int(input("how big do you want your board to be(choosing a size 3 (9 tiles) will have 31 moves allowed, and choosing a size 4(16 tiles) will have 80 moves allowed, otherwise you have infinite moves)? "))
board = getNewPuzzle(n)
turns = 0
over = False
while not isOver(board,turns,n):
    makeMove(board,nextMove(board))
    turns += 1
displayBoard(board)
if turns == 32 and n == 3:
        print("Best of luck next time!")
elif turns == 81 and n == 4:
        print("Best of luck next time!")
else:
    print("You did it! I'm proud of you")
