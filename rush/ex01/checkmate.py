def checkmate(board):
    pieces = 'PBRQ'
    chess_board = [i for i in board.split('\n')]
    size = len(chess_board)
    count_k = 0
    
    for line in chess_board:
        if len(line) != size:
            return f'Error: The board is not a square'
        count_k += line.count('K')
    
    if count_k > 1:
        return f'Error: There are {count_k} kings'
    elif count_k == 0:
        return f'Error: There is no king'

    for y in range(len(chess_board)):
        for x in range(len(chess_board)):
            if chess_board[y][x] == 'P':
                if (y > 0 and x > 0) and chess_board[y-1][x-1] == 'K':
                    return 'Success'
                elif (y > 0 and x < size - 1) and chess_board[y-1][x+1] == 'K':
                    return 'Success'
            if chess_board[y][x] == 'Q' or chess_board[y][x] == 'B':
                up_left = 1
                while y-up_left >= 0 and x-up_left >= 0:
                    if chess_board[y-up_left][x-up_left] == 'K':
                        return 'Success'
                    elif chess_board[y-up_left][x-up_left] in pieces:
                        break
                    up_left += 1
                up_right = 1
                while y-up_right >= 0 and x+up_right < size:
                    if chess_board[y-up_right][x+up_right] == 'K':
                        return 'Success'
                    elif chess_board[y-up_right][x+up_right] in pieces:
                        break
                    up_right += 1
                down_left = 1
                while y+down_left < size and x-down_left >= 0:
                    if chess_board[y+down_left][x-down_left] == 'K':
                        return 'Success'
                    elif chess_board[y+down_left][x-down_left] in pieces:
                        break
                    down_left += 1
                down_right = 1
                while y+down_right < size and x+down_right < size:
                    if chess_board[y+down_right][x+down_right] == 'K':
                        return 'Success'
                    elif chess_board[y+down_right][x+down_right] in pieces:
                        break
                    down_right += 1
            if chess_board[y][x] == 'Q' or chess_board[y][x] == 'R':
                up = 1
                while y-up >= 0:
                    if chess_board[y-up][x] == 'K':
                        return 'Success'
                    elif chess_board[y-up][x] in pieces:
                        break
                    up += 1
                down = 1
                while y+down < size:
                    if chess_board[y+down][x] == 'K':
                        return 'Success'
                    elif chess_board[y+down][x] in pieces:
                        break
                    down += 1
                left = 1
                while x-left >= 0:
                    if chess_board[y][x-left] == 'K':
                        return 'Success'
                    elif chess_board[y][x-left] in pieces:
                        break
                    left += 1
                right = 1
                while x+right < size:
                    if chess_board[y][x+right] == 'K':
                        return 'Success'
                    elif chess_board[y][x+right] in pieces:
                        break
                    right += 1
    return 'Fail'
    
def avoid_check(board):
    is_checkmate = True
    chess_board = [i for i in board.split('\n')]
    king_x, king_y = get_king_position(chess_board)
    last_index = len(chess_board) - 1
    available_board = [list(row) for row in chess_board]

    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            test_x = king_x + i
            test_y = king_y + j
            if test_x < 0 or test_x > last_index or test_y < 0 or test_y > last_index:
                continue
            test_board = chess_board.copy()
            test_board[king_y] = test_board[king_y][:king_x] + '.' + test_board[king_y][king_x + 1 :]
            test_board[test_y] = test_board[test_y][:test_x] + 'K' + test_board[test_y][test_x + 1 :]
            str_board = "\n".join(test_board)
            if checkmate(str_board) == 'Fail':
                is_checkmate = False
                available_board[test_y][test_x] = '\033[92m' + available_board[test_y][test_x] + '\033[97m'
    
    solution = "\n".join("".join(row) for row in available_board)
    return solution if not is_checkmate else 'Checkmate'
    
def get_king_position(chess_board):
    for row in range(len(chess_board)):
        if 'K' in chess_board[row]:
            king_y = row
            king_x = chess_board[row].index('K')
            
    return(king_x, king_y)