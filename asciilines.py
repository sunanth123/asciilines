##Sunanth Sakthivel
##CS510 HW 1

import sys

##this is a helper function that ensures that the canvas size is valid. return
##-1 if invalid.
def boundcheck(row_start,col_start):
    if row_start >= row:
        return -1
    if col_start >= col:
        return -1
    else:
        return 0

##this is a helper function that will ultimately draw out the board given
## a command with the characterl to fill with, the row start, column col start,
## whether its vertical or horizontal and length of how many characters to fill.
def create(board, fill, row_start, col_start, pos, length):
    ##if canvas is invalid then return an error
    if boundcheck(row_start,col_start) == -1:
        return

    ##if vertical line is drawn do the below
    if pos == 'v':
        ##if column start is less than 0 then return
        if col_start < 0:
            return
        ##if row start is less than 0 then calculate offset for length
        elif row_start < 0:
            length = length + row_start
            if length < 0:
                return
            row_start = 0

        ##determine the bound of how far out the characters will be drawn out
        if length + row_start < row:
            bound = length + row_start
        else:
            bound = row

        ##fill the canvas vertically from row start to bound with fill char.
        for i in range(row_start,bound):
            board[i][col_start] = fill

    ##else if the line is horizontal then do below
    else:
        ##if row start is less than 0 then return
        if row_start < 0:
            return
        ##if col start is less than 0 then calculate offset for length
        elif col_start < 0:
            length = length + col_start
            if length < 0:
                return
            col_start = 0

        ##determine the bound of how far out the characters will be drawn out
        if length + col_start < col:
            bound = length + col_start
        else:
            bound = col

        ##fill the canvas horizontally from col start to bound with fill char.
        for i in range(col_start,bound):
            board[row_start][i] = fill

    return board

##helper function that is used to check that the row and column size requested
##is valid. If not valid return 0.
def check_canvas(canvas_size):
    result = canvas_size.split(" ")
    check = [int(i) for i in result]
    if check[0] < 1 or check[1] < 1:
        return 0
    else:
        return 1

##helper function that checks to make sure the commands have only 5 actions
##ensure that 4th action is either 'h' or 'v' for horizontal and vertical
##respectively. And lastly to check if 5th action is a length that is greater
##than 0. If any of the commands are invalid then 0 is returned.
def check_commands(commands):
    for command in commands:
        check = command.split(" ")
        if len(check) != 5:
            return 0
        if check[3] != 'h' and check[3] != 'v':
            return 0
        if int(check[4]) < 1:
            return 0
    return 1

##this is a helper function that parses a string returns the row and column
##values as int. The input is a string for example: "4 3"
def get_size(canvas_size):
    result = canvas_size.split(" ")
    check = [int(i) for i in result]
    return check[0],check[1]

##This helper function will initialize a board with row x col dimensions all
##filled with the '.' character.
def generate_board(board,row,col):
    board = [["."]*col for _ in range(row)]
    return board

##uses the create helper function to process all the commands and draw the
##final board.
def draw_board(board,row,col,commands):
    ##for loop that processes each command by parsing the respective command
    ##into variables which are then passed to the create function to draw
    ##the board.
    for command in commands:
        instructions = command.split(" ")
        fill = instructions[0]
        row_start = int(instructions[1])
        col_start = int(instructions[2])
        pos = instructions[3]
        length = int(instructions[4])
        board = create(board, fill, row_start, col_start, pos, length)
    return board

##print out the final board to standard output
def print_canvas(board):
    for row in board:
    	print("".join(row))

if __name__ == '__main__':
    row = 0
    col = 0
    board = []

    ##if more than 2 arguments or no path is given then print out the
    ##respective error messages
    if len(sys.argv) > 2:
        print("Need to provide only one path to .tvg file")
        sys.exit()
    elif len(sys.argv) == 1:
        print("please provide a path to a .tvg file to run program")
        sys.exit()

    ##open the file using the path that is passed as a command line arg.
    ##make sure that the path is to a .tvg file
    filename = sys.argv[1]
    with open(filename) as f:
        data = f.read().splitlines()

    ##the first line will include the canvas size info and the rest of the
    ##lines will include the commands so split accordingly.
    canvas_size, commands = data[0], data[1:]

    ##if canvas has invalid size request then print error.
    if check_canvas(canvas_size) == 0:
        print("Invalid canvas size found")
        sys.exit()

    ##if any of the commands parsed from .tvg file are invalid then print error.
    if check_commands(commands) == 0:
        print("invalid command as input")
        sys.exit()

    ##draw out the board using the information that is parsed from the .tvg file
    row,col = get_size(canvas_size)
    board = generate_board(board,row,col)
    board = draw_board(board,row,col,commands)
    ##canvas is printed out to the standard output.
    print_canvas(board)
