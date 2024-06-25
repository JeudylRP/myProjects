"""

def print_board(board):
    
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):

    # Überprüfen der Zeilen
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Überprüfen der Spalten
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Überprüfen der Diagonalen
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def tictactoe():

    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    turns = 0

    print("Willkommen bei Tic Tac Toe!")
    print_board(board)

    while turns < 9:
        print(f"Aktueller Spieler: {current_player}")
        try:
            row = int(input("Wähle eine Zeile (0, 1, 2): "))
            col = int(input("Wähle eine Spalte (0, 1, 2): "))
        except ValueError:
            print("Ungültige Eingabe! Bitte gib eine Zahl zwischen 0 und 2 ein.")
            continue

        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Ungültige Eingabe! Bitte gib eine Zahl zwischen 0 und 2 ein.")
            continue

        if board[row][col] == " ":
            board[row][col] = current_player
            turns += 1
            print_board(board)

            if check_win(board, current_player):
                print(f"Spieler {current_player} hat gewonnen!")
                break

            current_player = "O" if current_player == "X" else "X"
        else:
            print("Ungültiger Zug! Das Feld ist bereits belegt. Versuche es erneut.")

    if turns == 9:
        print("Das Spiel endet unentschieden.")

if __name__ == "__main__":
    tictactoe()
"""

print("Hello Word")