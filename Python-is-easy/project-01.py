def main():
    def checkRows(player):
        for i in range(5):
            for j in range(3):
                if field[i][j] == signs[player] and field[i + 1][j] == signs[player] and field[i + 2][j] == signs[player] and field[i + 3][j] == signs[player]:
                    return True
        return False

    def checkColumns(player):
        for i in range(6):
            for j in range(2):
                if field[i][j] == signs[player] and field[i][j + 1] == signs[player] and field[i][j + 2] == signs[player] and field[i][j + 3] == signs[player]:
                    return True
        return False

    def checkDiagonal(player):
        for i in range(3):
            for j in range(3, 5):
                if field[i][j] == signs[player] and field[i + 1][j - 1] == signs[player] and field[i + 2][j - 2] == signs[player] and field[i + 3][j - 3] == signs[player]:
                    return True

        for i in range(3):
            for j in range(2):
                if field[i][j] == signs[player] and field[i + 1][j + 1] == signs[player] and field[i + 2][j + 2] == signs[player] and field[i + 3][j + 3] == signs[player]:
                    return True
        
        return False
        
    def checkForWinner(player):
        if (checkRows(player) == True or checkColumns(player) == True or checkDiagonal(player) == True):
            return True
        else:
            return False    
        
    def drawField(field):
        for row in range(9):
            if row % 2 == 0:
                practicalRow = int(row / 2)

                for col in range(11):

                    if col % 2 == 0:
                        practicalCol = int(col / 2)

                        if col != 10:
                            print(field[practicalCol][practicalRow], end='')
                        else:
                            print(field[practicalCol][practicalRow])
                    else:
                        if col != 10:
                            print('|', end='')
                        else:
                            print('|')
            else:
                print('-----------')       

    field = [
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ']
    ];

    drawField(field)

    isWinner = False
    player = 1
    signs = {1: 'X', 2: 'O'}

    while isWinner == False:
    
        col = int(input("Choose your column: "))
        row = int(input("Choose your row: "))
            
        if field[col][row] == ' ':
            sign = signs[player]
            field[col][row] = sign

        isWinner = checkForWinner(player)

        if isWinner:
            drawField(field)
            print(f'Congratulations! Player {player} wins!')
            return

        if player == 1:
            player = 2
        else:
            player = 1

        drawField(field)


main()
