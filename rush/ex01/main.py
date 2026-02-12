import sys
from checkmate import checkmate, avoid_check

def main():
    
    for i in range(1, len(sys.argv)):
        with open(sys.argv[i], 'r', encoding='utf-8') as f:
            board = f.read()
            print(f"Board #{i} ------------------------------")
            print()
            print(board)
            print()
            result = checkmate(board)
            if result == 'Success':
                print(result)
                solution = avoid_check(board)
                if solution == 'Checkmate':
                    print('Checkmate! The King has no moves left.')
                else:
                    print('The King is in check! Here are the possible moves:')
                    print()
                    print(solution)
            else:
                print(result)
            print()

if __name__ == "__main__":
    main()
