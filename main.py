import chess
from movegeneration import next_move

depth=3

def start():

    board = chess.Board()
    side=input("Start as [w]hite or [b]lack:\n")

    if side=='w':
        user_side=chess.WHITE
    else:
        user_side=chess.BLACK

    if user_side == chess.WHITE:
        print(render(board))
        board.push(get_move(board))

    while not board.is_game_over():
        board.push(next_move(depth, board))
        print(render(board))
        board.push(get_move(board))

    print(f"\nResult: [w] {board.result()} [b]")


def render(board):

    board_string = list(str(board))

    uni_pieces = {
        "R": "♖",
        "N": "♘",
        "B": "♗",
        "Q": "♕",
        "K": "♔",
        "P": "♙",
        "r": "♜",
        "n": "♞",
        "b": "♝",
        "q": "♛",
        "k": "♚",
        "p": "♟",
        ".": "·",
    }
    for i, char in enumerate(board_string):
        if char in uni_pieces:
            board_string[i] = uni_pieces[char]
    ranks = ["1", "2", "3", "4", "5", "6", "7", "8"]
    display = []
    for rank in "".join(board_string).split("\n"):
        display.append(f"  {ranks.pop()} {rank}")
    if board.turn == chess.BLACK:
        display.reverse()
    display.append("    a b c d e f g h")
    return "\n" + "\n".join(display)


def get_move(board):

    move = input(f"\nYour move :\n")

    for legal_move in board.legal_moves:
        if move == str(legal_move):
            return legal_move
    return get_move(board)


start()
