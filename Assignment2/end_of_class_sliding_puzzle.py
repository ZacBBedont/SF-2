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
    print(empty_tile)
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

board = getNewPuzzle(3)
nextMove(board)