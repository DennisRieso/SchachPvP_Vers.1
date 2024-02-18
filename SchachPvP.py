import chess

def display_board(board):
    print(board)

if __name__ == "__main__":
    # Erstelle ein Schachbrett
    board = chess.Board()

    while not board.is_game_over():
        # Anzeige des aktuellen Schachbretts
        display_board(board)

        # Benutzereingabe für den Zug (Abwechselnd)
        move_str = input("Gib deinen Zug im Standard-Algebraischen Format (z.B. e2e4) ein: ")

        try:
            # Zugberechnung/Zugprüfung
            move = chess.Move.from_uci(move_str)
            if move in board.legal_moves:
                board.push(move)
            else:
                print("Ungültiger Zug. Bitte erneut versuchen.")
        except ValueError:
            print("Ungültige Eingabe. Bitte im Standard-Algebraischen Format (z.B. e2e4) eingeben.")
    
    # Spielende: Anzeige der letzten Schachstellung
    display_board(board)
    print("Spiel vorbei.")

