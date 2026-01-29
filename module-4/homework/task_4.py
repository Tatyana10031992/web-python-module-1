import random

def print_board(board):
    print("\n" + "-" * 21)
    for row in board:
        print("|", end="")
        for cell in row:
            print(f"{cell:2d} |" if cell != 0 else "   |", end="")
        print("\n" + "-" * 21)

def is_solved(board):
    expected = list(range(1, 16)) + [0]
    flat = [cell for row in board for cell in row]
    return flat == expected

def find_empty(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                return i, j
    return None

def can_move(board, direction):
    i, j = find_empty(board)
    if direction == "w" and i > 0:
        return True
    if direction == "s" and i < 3:
        return True
    if direction == "a" and j > 0:
        return True
    if direction == "d" and j < 3:
        return True
    return False

def make_move(board, direction):
    i, j = find_empty(board)
    if direction == "w" and i > 0:
        board[i][j], board[i-1][j] = board[i-1][j], board[i][j]
    elif direction == "s" and i < 3:
        board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
    elif direction == "a" and j > 0:
        board[i][j], board[i][j-1] = board[i][j-1], board[i][j]
    elif direction == "d" and j < 3:
        board[i][j], board[i][j+1] = board[i][j+1], board[i][j]

def shuffle_board():
    board = [[1, 2, 3, 4],
             [5, 6, 7, 8],
             [9, 10, 11, 12],
             [13, 14, 15, 0]]
    directions = ["w", "a", "s", "d"]
    for _ in range(200):
        valid_moves = [d for d in directions if can_move(board, d)]
        move = random.choice(valid_moves)
        make_move(board, move)
    return board

def main():
    print("Добро пожаловать в «Пятнашки»!")
    input("Нажмите Enter, чтобы начать...")
    board = shuffle_board()
    moves_counter = 0
    while True:
        print_board(board)
        print(f"Ходы: {moves_counter}")

        if is_solved(board):
            print("Поздравляем! Вы решили головоломку!")
            break

        cmd = input("Ваш ход (W/A/S/D) или Q для выхода: ").strip().lower()

        if cmd == 'q':
            print("Игра завершена.")
            break
        elif cmd in ['w', 'a', 's', 'd']:
            if can_move(board, cmd):
                make_move(board, cmd)
                moves_counter += 1
            else:
                print("Невозможный ход! Попробуйте другой.")
        else:
            print("Некорректная команда! Используйте W/A/S/D или Q.")

if __name__ == "__main__":
    main()