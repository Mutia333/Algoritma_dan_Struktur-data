#Mentahan Tic Tac Toe

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Cek baris
    for row in board:
        if all([cell == player for cell in row]):
            return True
    # Cek kolom
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    # Cek diagonal
    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

def is_full(board):
    return all([cell != " " for row in board for cell in row])

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        try:
            move = input(f"Giliran {current_player}, masukkan posisi (baris kolom, contoh 1 3): ")
            row, col = map(int, move.split())
            row -= 1
            col -= 1
            if board[row][col] != " ":
                print("Sudah terisi, coba lagi!")
                continue
        except:
            print("Input salah, gunakan format 'baris kolom', misal '1 3'.")
            continue

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Selamat! Pemain {current_player} menang!")
            break
        if is_full(board):
            print_board(board)
            print("Seri!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()