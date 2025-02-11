board = {
    1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' '
}

def markBoard(position, mark):
    if board[position] == ' ':
        board[position] = mark
        return True
    else:
        return False

def printBoard():
    for i in range(1,10):
        if board[i] == ' ':
            print(i, end=' ')
        else:
            print(board[i], end=' ')

        if i % 3 == 0:
            print()
        else:
            print('|', end=' ')

def validateMove(position):
    if isinstance(position, str):
        position = int(position) if position.isdigit() else None

    if not isinstance(position, int) or position < 1 or position > 9:
        return False

    if board.get(position) != ' ':
        return False

    return True

winCombinations = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [1, 5, 9],
    [3, 5, 7]
]

def checkWin(player):
    for combo in winCombinations:
        if all(board[pos] == player for pos in combo):
            return True
    return False

def checkFull():
    return all(board[pos] != ' ' for pos in board) and not any(checkWin(mark) for mark in ['X', 'O'])

gameEnded = False
currentTurnPlayer = 'X'

print('Game started: \n\n' +
    ' 1 | 2 | 3 \n' +
    ' --------- \n' +
    ' 4 | 5 | 6 \n' +
    ' --------- \n' +
    ' 7 | 8 | 9 \n')

def playGame():
    global currentTurnPlayer
    global gameEnded

    while not gameEnded:
        printBoard()
        move = input(currentTurnPlayer + "'s turn, input: ")

        if not move.isdigit() or not validateMove(int(move)):
            print("Invalid move. Try again.")
            continue

        markBoard(int(move), currentTurnPlayer)

        if checkWin(currentTurnPlayer):
            print("Player " + currentTurnPlayer + " wins!")
            gameEnded = True
        elif checkFull():
            print("It's a tie!")
            gameEnded = True

        if not gameEnded:
            currentTurnPlayer = 'O' if currentTurnPlayer == 'X' else 'X'

playGame()
