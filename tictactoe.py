
#Draw Board
def drawBoard(board):
    print( str(board[0]) + ' | ' + str(board[1]) + ' | ' + str(board[2]))
    print('----------')
    print( str(board[3]) + ' | ' + str(board[4]) + ' | ' + str(board[5]))
    print('----------')
    print( str(board[6]) + ' | ' + str(board[7]) + ' | ' + str(board[8]))

#Setup the game
def selectPiece():
    while True:
        player1 = str(input().upper())
        if player1 == 'O':
            player2 = 'X'
            return player1, player2
        elif player1 == 'X':
            player2 = 'O'
            return player1, player2
        else:
            print("Incorrect entry, please enter X or O.")

def setup():
    moves = [i for i in range(1,10)]
    board = [' '] * 10 
    print("Welcome to tic tac toe. Make moves by entering a number 1-9.")
    print("These numbers correspond to the board as follows")
    drawBoard([i for i in range(1,10)])
    print("Player 1, do you want to be X or O ?")
    player1, player2 = selectPiece()
    return player1, player2, moves, board
   

#Asks for input and makes moves 
def makeMove(board, player, moves):
    while True:
        try :
            move = int(input("Please make your move (enter a number from 1-9)"))
            if move in moves:
                board[move-1] = player
                moves.remove(move)
                return board, moves
        except ValueError:
            print('Invalid entry. Try again')
        else:
            print('Move already taken. Try again')
        
#function for AI input (start with random for now)

#function to check if there's a winner (vertical, horizontal, diagonal)
def winner(board, currentplayer):
    winners=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    indexlist = [i for i, value in enumerate(board) if value == currentplayer] 
    for i in winners:
        count = 0
        for x in i:
            if x in indexlist: 
                count += 1
                if count == 3: 
                    return True

    


#def winner(board)

#Ask if user wants to play again, reset board

#main gameplay function
player1, player2, moves, board = setup()
currentplayer = player1

while True:
    drawBoard(board)
    print(currentplayer + "'s turn")
    board, moves = makeMove(board, currentplayer, moves)
    if winner(board, currentplayer) == True:
        drawBoard(board)
        print(currentplayer + ' won!')
        repeat = str(input('Want to play again? (Y/N)').upper())
        if repeat == 'Y':
            player1, player2, moves, board = setup()
        else:
            break
    if len(moves) == 0:
        repeat = str(input('Game Over. No Winner. Want to play again? (Y/N)').upper())
        if repeat == 'Y':
            player1, player2, moves, board = setup()
        else: 
            break
    if currentplayer == player1:
        currentplayer = player2
    elif currentplayer == player2:
        currentplayer = player1
    



