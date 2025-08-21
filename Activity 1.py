Board={'7': ' ', '8': ' ', '9': ' ',
         '4': ' ', '5': ' ', '6': ' ',
         '1': ' ', '2': ' ', '3': ' ',}
boardkeys=[]
for key in Board:
    boardkeys.append(key)

def printBoard():
    print(Board['7'] + '|' + Board['8'] + '|' + Board['9'])
    print('-+-+-')
    print(Board['4'] + '|' + Board['5'] + '|' + Board['6'])
    print('-+-+-')
    print(Board['1'] + '|' + Board['2'] + '|' + Board['3'])

def game():
    turn = 'X'
    count = 0
    for i in range(10):
        printBoard()  # <-- Remove Board argument
        print("It's your turn," + turn + ". Move to which place? (1-9)")
        move = input()
        if move not in Board:
            print("Invalid move. Please choose a number from 1 to 9.")
            continue
        if Board[move] == ' ':
            Board[move] = turn
            count += 1
        else:
            print("That place is already filled. Choose another place.")
            continue
        if count >= 5:
            if (Board['7'] == Board['8'] == Board['9'] != ' ') or \
               (Board['4'] == Board['5'] == Board['6'] != ' ') or \
               (Board['1'] == Board['2'] == Board['3'] != ' ') or \
               (Board['7'] == Board['4'] == Board['1'] != ' ') or \
               (Board['8'] == Board['5'] == Board['2'] != ' ') or \
               (Board['9'] == Board['6'] == Board['3'] != ' ') or \
               (Board['7'] == Board['5'] == Board['3'] != ' ') or \
               (Board['9'] == Board['5'] == Board['1'] != ' '):
                printBoard()
                print("Player " + turn + " wins!")
                break
        if count == 9:
            printBoard()
            print("It's a draw!")
            break
        turn = 'O' if turn == 'X' else 'X'

    restart = input("Do you want to play again? (yes/no): ")
    if restart.lower() == 'yes':
        for key in boardkeys:
            Board[key] = ' '
        game()
if __name__ == "__main__":
        game()
         