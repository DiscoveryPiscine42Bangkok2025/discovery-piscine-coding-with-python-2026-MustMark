def checkmate(board):
    pieces = 'PBRQ'
    chess_board = [i for i in board.split('\n')]
    size = len(chess_board)
    count_k = 0

    for line in chess_board:
        if len(line) != size:
            print('Error: The board is not a square')
            return
        count_k += line.count('K')
    
    if count_k > 1:
        print(f'Error: There are {count_k} kings')
        return
    elif count_k == 0:
        print('Error: There is no king')
        return
        
    for y in range(len(chess_board)):
        for x in range(len(chess_board)):
            if chess_board[y][x] == 'P':
                if (y > 0 and x > 0) and chess_board[y-1][x-1] == 'K':
                    print('Success')
                    return
                elif (y > 0 and x < size - 1) and chess_board[y-1][x+1] == 'K':
                    print('Success')
                    return
            if chess_board[y][x] == 'Q' or chess_board[y][x] == 'B':
                up_left = 1
                while y-up_left >= 0 and x-up_left >= 0:
                    if chess_board[y-up_left][x-up_left] == 'K':
                        print('Success')
                        return
                    elif chess_board[y-up_left][x-up_left] in pieces:
                        break
                    up_left += 1
                up_right = 1
                while y-up_right >= 0 and x+up_right < size:
                    if chess_board[y-up_right][x+up_right] == 'K':
                        print('Success')
                        return
                    elif chess_board[y-up_right][x+up_right] in pieces:
                        break
                    up_right += 1
                down_left = 1
                while y+down_left < size and x-down_left >= 0:
                    if chess_board[y+down_left][x-down_left] == 'K':
                        print('Success')
                        return
                    elif chess_board[y+down_left][x-down_left] in pieces:
                        break
                    down_left += 1
                down_right = 1
                while y+down_right < size and x+down_right < size:
                    if chess_board[y+down_right][x+down_right] == 'K':
                        print('Success')
                        return
                    elif chess_board[y+down_right][x+down_right] in pieces:
                        break
                    down_right += 1
            if chess_board[y][x] == 'Q' or chess_board[y][x] == 'R':
                up = 1
                while y-up >= 0:
                    if chess_board[y-up][x] == 'K':
                        print('Success')
                        return
                    elif chess_board[y-up][x] in pieces:
                        break
                    up += 1
                down = 1
                while y+down < size:
                    if chess_board[y+down][x] == 'K':
                        print('Success')
                        return
                    elif chess_board[y+down][x] in pieces:
                        break
                    down += 1
                left = 1
                while x-left >= 0:
                    if chess_board[y][x-left] == 'K':
                        print('Success')
                        return
                    elif chess_board[y][x-left] in pieces:
                        break
                    left += 1
                right = 1
                while x+right < size:
                    if chess_board[y][x+right] == 'K':
                        print('Success')
                        return
                    elif chess_board[y][x+right] in pieces:
                        break
                    right += 1
    print('Fail')