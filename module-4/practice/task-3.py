def print_board(board):
    for row in board:
        print(" ".join(f"{cell:2d}" for cell in row))
    print()
    
def is_valid(x, y, n, board):
    return 0 <= x < n and 0 <= y < n and board[x][y] == -1

def solve_knight_tour(board, x, y, move_count, n, moves):
    
    if move_count == n * n:
        return True
    
    for dx, dy in moves:
        next_x = x + dx
        next_y = y + dx
        
        if is_valid(next_x, next_y, n, board):
            board[next_x][next_y] = move_count + 1
            
            if solve_knight_tour(board,next_x, next_y, move_count + 1, n, moves):
                return True
            board[next_x][next_y] = -1
            
    return False

def main():
    n = 6
    
    moves = [
        (2,1), (1,2), (-1,2), (-2,1),
        (-2,-1), (-1,-2), (1,-2), (2, -1)
    ]
    
    board = [[-1 for _ in range(n)] for _ in range(n)]
    
    try:
        x = int(input(f"Введите начальную строку (0-{n-1}):"))
        y = int(input(f"Введите начальный столбец (0-{n-1}):"))
        if not (0 <= x < n and 0 <= y < n):
            print("Координаты вне доски!")
            return
    except ValueError:
        print("Введите числа!")
        return
    
    board[x][y] = 1
    
    print(f"\nПоиск маршрута для доски {n}×{n} с начальной клетки ({x}, {y})...\n")


 
    if solve_knight_tour(board, x, y, 1, n, moves):
        print("Маршрут найден!\n")
        print_board(board)
    else:
        print("Маршрут не найден. Попробуйте другую начальную клетку.")


if __name__ == "__main__":
    main()