import tkinter as tk
from tkinter import messagebox


board = [""] * 9


def check_winner():
    wins = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for a, b, c in wins:
        if board[a] == board[b] == board[c] and board[a] != "":
            return board[a]

    if "" not in board:
        return "Draw"

    return None


def minimax(ai_turn):
    result = check_winner()

    if result == "O":
        return 1

    if result == "X":
        return -1

    if result == "Draw":
        return 0

    if ai_turn:
        best_score = -100

        for i in range(9):
            if board[i] == "":
                board[i] = "O"

                score = minimax(False)

                board[i] = ""

                if score > best_score:
                    best_score = score

        return best_score

    else:
        best_score = 100

        for i in range(9):
            if board[i] == "":
                board[i] = "X"

                score = minimax(True)

                board[i] = ""

                if score < best_score:
                    best_score = score

        return best_score


def computer_move():
    best_score = -100
    best_move = None

    for i in range(9):
        if board[i] == "":
            board[i] = "O"

            score = minimax(False)

            board[i] = ""

            if score > best_score:
                best_score = score
                best_move = i

    if best_move is not None:
        board[best_move] = "O"
        buttons[best_move].config(text="O")

    check_game()


def player_move(position):
    if board[position] != "":
        return

    board[position] = "X"
    buttons[position].config(text="X")

    if check_winner() is not None:
        check_game()
        return

    status_label.config(text="Computer's turn...")

    window.after(300, computer_move)


def check_game():
    result = check_winner()

    if result == "X":
        messagebox.showinfo("Game Over", "You Win!")
        reset_game()

    elif result == "O":
        messagebox.showinfo("Game Over", "Computer Wins!")
        reset_game()

    elif result == "Draw":
        messagebox.showinfo("Game Over", "It's a Draw!")
        reset_game()

    else:
        status_label.config(text="Your turn (X)")


def reset_game():
    global board

    board = [""] * 9

    for button in buttons:
        button.config(text="")

    status_label.config(text="Your turn (X)")


# Main window
window = tk.Tk()
window.title("AI Tic-Tac-Toe")
window.geometry("400x500")
window.resizable(False, False)


title_label = tk.Label(
    window,
    text="AI Tic-Tac-Toe",
    font=("Arial", 24, "bold")
)
title_label.pack(pady=20)


status_label = tk.Label(
    window,
    text="Your turn (X)",
    font=("Arial", 14)
)
status_label.pack(pady=10)


game_frame = tk.Frame(window)
game_frame.pack()


buttons = []

for i in range(9):
    button = tk.Button(
        game_frame,
        text="",
        font=("Arial", 30, "bold"),
        width=4,
        height=2,
        command=lambda i=i: player_move(i)
    )

    button.grid(
        row=i // 3,
        column=i % 3,
        padx=3,
        pady=3
    )

    buttons.append(button)


restart_button = tk.Button(
    window,
    text="Restart Game",
    font=("Arial", 13),
    command=reset_game
)
restart_button.pack(pady=20)


window.mainloop()
