
#Draw Board
def drawBoard(board):
    print( str(board[0]) + ' | ' + str(board[1]) + ' | ' + str(board[2]))
    print('----------')
    print( str(board[3]) + ' | ' + str(board[4]) + ' | ' + str(board[5]))
    print('----------')
    print( str(board[6]) + ' | ' + str(board[7]) + ' | ' + str(board[8]))

#Setup the game    
def setup():
    moves = list(range(1,10))
    board = [' '] * 10 
    print("Welcome to tic tac toe. Make moves by entering a number 1-9.")
    print("These numbers correspond to the board as follows")
    drawBoard(moves)
    while True:
        player1 = str(input("Player 1, do you want to be X or O ?").upper())
        if player1 == 'O':
            player2 = 'X'
            return player1, player2, moves, board
        elif player1 == 'X':
            player2 = 'O'
            return player1, player2, moves, board
        else:
            print("Invalid entry, please enter X or O.")    

#Ask for input and record moves 
def makeMove(board, player, moves):
    while True:
        try:
            move = int(input("Please make your move (enter a number from 1-9)"))
            if move in moves: #checks if the move is available
                board[move-1] = player #records the move on the board
                moves.remove(move) #removes the current move from future move options
                return board, moves
        except ValueError:
            print('Invalid entry. Try again')
        else:
            print('Move already taken. Try again')

#Checks if there's a winner
def winner(board, currentplayer):
    winners=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]] #winning board indices
    indexlist = [i for i, value in enumerate(board) if value == currentplayer] # returns indices of current player's moves
    for i in winners: #iterates through each winning combination to see if it exists on the board
        if set(i).issubset(set(indexlist)):
            return True

#Main gameplay
player1, player2, moves, board = setup() #setup the board
currentplayer = player1 #start with player 1

while True:
    drawBoard(board)
    print(currentplayer + "'s turn")
    board, moves = makeMove(board, currentplayer, moves) 
    if winner(board, currentplayer) == True: #Checks if there's a winner
        drawBoard(board)
        print(currentplayer + ' won!')
        if str(input('Want to play again? (Y/N)').upper()) == 'Y':
            player1, player2, moves, board = setup()
        else:
            break
    if len(moves) == 0: #Checks if the board is full
        if str(input('Game Over. No Winner. Want to play again? (Y/N)').upper()) == 'Y':
            player1, player2, moves, board = setup()
        else: 
            break
    if currentplayer == player1: #Switches plaers
        currentplayer = player2
    else:
        currentplayer = player1
    



