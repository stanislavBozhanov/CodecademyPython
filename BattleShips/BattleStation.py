from random import randint


def print_board(board):
    for row in board:
        print " ".join(row)


def random_row(board):
    return randint(0, len(board) - 1)


def random_col(board):
    return randint(0, len(board[0]) - 1)


#Game starts

board = []
player_shots = []
size_of_grid = int(raw_input("What size of grid would you want:"))
for rows in range(size_of_grid):
    board.append(["O"] * size_of_grid)
    player_shots.append(["O"] * size_of_grid)
print "Let's play Battleship!"
print_board(board)
number_of_ships = int(raw_input("Enter number of ships: "))
for ship in xrange(number_of_ships):
    while True:
        ship_row = random_row(board)
        ship_col = random_col(board)
        if board[ship_row][ship_col] == "O":
            board[ship_row][ship_col] = "X"
            break
print_board(board)
number_of_shots = int(raw_input("How many bullets do you have: "))
for turn in xrange(number_of_shots):
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))
    if guess_row < 0 or guess_row > size_of_grid -1 or guess_col < 0 or guess_col > size_of_grid - 1:
        print "Oops, that's not even in the ocean."
    elif board[guess_row][guess_col] == 'X':
        print "Congratulations! You sunk my battleship!"
        board[guess_row][guess_col] = '-'
        player_shots[guess_row][guess_col] = '-'
    elif board[guess_row][guess_col] == "-":
        print "You guessed that one already."
    else:
        print "You missed my battleship!"
        board[guess_row][guess_col] = "-"
        player_shots[guess_row][guess_col] = '-'
    win = True
    for row in range(size_of_grid):
        for col in range(size_of_grid):
            if board[row][col] == 'X':
                win = False
    if win:
        print "You won!"
        break
    print_board(player_shots)
    print "Turns remaining", number_of_shots - turn - 1

print "Game Over"
