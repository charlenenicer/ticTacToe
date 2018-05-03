theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '} 

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])



turn = 'X'
for i in range(9):
	printBoard(theBoard) # prints a new board each turn
	print('Turn for ' + turn + '. Move on which space?')
	move = input() # gets active player's move
	theBoard[move] = turn # updates game baord accordingly
	if turn == 'X': # swaps players turn
		turn = 'O'
	else: 
		turn = 'X'

# Fix
# 1. X/O can be placed on top of X/O (shouldn't be able to remove other player's X/O)
# 2. No winner declared after 3 straight X/O
# 3. Replace commands (e.g top-L) to key bind (e.g pressing 7 instead)
# 4. If player does not type in correct command / typo, turn is forgoed (fix this)





