"""Module for Tic-Tac-Toe."""

def draw_board(board):
    """
    Making the board appear in the game. 
    Doing this by printing the board 
    
    Parameters
    ----------
    board: string 
        Definition of the board.
    
    Returns 
    ----------
        Sets up layout of game  
    """

    print('\n')
    print(board[1] + '|' + board[2] + '|' +board[3])
    print('-|-|-')
    print(board[4] + '|' + board[5] + '|' +board[6])
    print('-|-|-')
    print(board[7] + '|' + board[8] + '|' +board[9])
    print('\n')

def check_win(board):
    """Check if the player wins.

    Setting them equal to eachother to check if there are 
    E.g. if 1 = x and 2 = x and 2 = 3, then 3 = x making a tic tac toe win
    
    Parameters
    ----------
    board : string 
        Checks winner of the board   
    
    Returns
    -------
    boolean 
        Specifies the winner 
    """
  
    if board[1] == board[2] and board[2] == board[3]:
        return True
    if board[4] == board[5] and board[5] == board[6]:
        return True
    if board[7] == board[8] and board[8] == board[9]:
        return True
    if board[1] == board[4] and board[4] == board[7]:
        return True
    if board[2] == board[5] and board[5] == board[8]:
        return True
    if board[3] == board[6] and board[6] == board[9]:
        return True
    if board[1] == board[5] and board[5] == board[9]:
        return True
    if board[3] == board[5] and board[5] == board[7]:
        return True
    
    return False

def check_game_over(board):
    """Check if the game is over.
    
    States that if any of the positions in the board 
    are numbers, then it the game is still going.
    if they are all X's and O's, 
    then the game is over.
    Also if move is not in the board
    Then it returns as invalid 
    
    Parameters
    ----------
    board : string
        Definition of the board.
    
    Returns
    -------
    boolean
        Indicates whether the game is over.
    """

    numList = ['1','2','3','4','5','6','7','8','9']
    for pos in board:
        if pos in numList:
            return False

    return True


def play_game():
    """
    This function is the start of the game.
    """
   
    # game starts here-variable for the board 
    board = ['#','1','2','3','4','5','6','7','8','9']

    playing = True

    # doing this draws the board 
    draw_board(board)

    # game starts here 
    while playing:

        print("Player 1 (X), make your move! (Pick a number 1-9)")
        move = input()

        if move not in board:
            print ('Invalid! Please enter a value 1-9')
            continue

        board[int(move)] = 'X'
        draw_board(board)

        #checks if player one won 
        if check_win(board):
            print("Player 1 wins. Good job!")
            break

        #if they did it makes 
        if check_game_over(board):
            print("Game over, no one won :(")
            break


        #makes a move, and whichever move they make-insert = 
        print("Player 2 (O), make your move! (Pick a number 1-9)")
        move = input()

        if move not in board:
            print ('Invalid! Please enter a value 1-9')
            continue

        board[int(move)] = 'O'
        draw_board(board)

        if check_win(board):
            print("player 2 wins. Good job!")
            break

        if check_game_over(board):
            print("Game over, no one won :(")
            break