from random import randint
x = randint(0,1)
p1w = 0
p2w = 0
def gameplay(x):
    global board
    if x == 0:
        current = 'P1'
    else:
        current = 'P2'
    boardloading()
    for abc in range(9):
        checkline(board)
        if current == 'P1':
            move = int(input('Player 1 turn - Please choose a place: '))
            while board[move-1] == 'O' or board[move-1] == 'X':
                move = int(input('Please choose another place: '))
            board[move-1] = 'X'
            boardloading()
            current = 'P2'
        elif current == 'P2':
            move = int(input('Player 2 turn - Please choose a place: '))
            while board[move-1] == 'O' or board[move-1] == 'X':
                move = int(input('Please choose another place: '))
            board[move-1] = 'O'
            boardloading()
            current = 'P1'
def boardloading():
    for o in range (9):
        if o == 2 or o == 5 or o == 8:
            print(board[o],'\n')
        else:
            print(board[o], end = ' | ')
def winnercheck(board,i,n,x):
    global p1w
    global p2w
    if board[i] == 'X' and x == 0:
        p1w += 1
    elif board[i] == 'O' and x == 0:
        p2w += 1
    elif board[i] == 'X' and x == 1:
        p2w += 1
    else:
        p1w += 1
    if p1w > (n//2):
        return 'Player 1 wins'
    elif p2w > (n//2):
        return 'Player 2 wins'
def checkline(board):
    for i in range(7):
        if (i == 0 or i == 3 or i == 6) and board[i] == board[i+1] == board[i+2]:
            winnercheck(board,i,n,x)
            return p1w,p2w
        elif (i == 0 or i == 1 or i == 2) and board[i] == board[i+3] == board[i+6]:
            winnercheck(board,i,n,x)
            return p1w,p2w
        elif i == 4 and (board[i-4] == board[i] == board[i+4] or board[i-2] == board[i] == board[i+2]):
            winnercheck(board,i,n,x)
            return p1w,p2w
if x == 0:
    p1 = 'X'
    p2 = 'O'
else:
    p1 = 'O'
    p2 = 'X'
print('Player 1 plays with {}, Player 2 plays with {}'.format(p1,p2))
n = int(input('How many matches you want to play?'))
for i in range (n):
    board = [o for o in range(1,10)]
    gameplay(x)
