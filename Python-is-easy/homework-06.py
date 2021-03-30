def create_board(rows, cols):
    for row in range(rows * 2 - 1):
        if row % 2 == 0:
            for col in range(1, cols * 2):
                if col % 2 != 0:
                    if col != cols * 2 - 1:
                        print(" ", end="")
                    else:
                        print(" ")
                else:
                    print("|", end="")
        else:
            print('-' * (cols * 2))
    return True


create_board(3, 6)
