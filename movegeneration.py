import chess
from evaluate import evaluate_board, move_value, check_end_game


MATE = 1000000000
MATE_MAX = 999000000


def next_move(depth, board):

    move = minimax_root(depth, board)
    return move


def get_ordered_moves(board):
    end_game = check_end_game(board)

    def orderer(move):
        return move_value(board, move, end_game)

    in_order = sorted(
        board.legal_moves, key=orderer, reverse=(board.turn == chess.WHITE)
    )
    return list(in_order)


def minimax_root(depth, board):

    maximizing_player = (board.turn == chess.WHITE)
    if maximizing_player:
        best_score = float('-inf')
    else:
        best_score = float('inf')
    best_move = None

    for move in get_ordered_moves(board):
        board.push(move)
        score = minimax(depth - 1, board, float('-inf'),
                        float('inf'), not maximizing_player)
        board.pop()

        if maximizing_player and score > best_score:
            best_score = score
            best_move = move
        elif not maximizing_player and score < best_score:
            best_score = score
            best_move = move

    return best_move


def minimax(depth, board, alpha, beta, is_maximising_player):
    if is_maximising_player:
        return max_value(depth, board, alpha, beta)
    else:
        return min_value(depth, board, alpha, beta)


def max_value(depth, board, alpha, beta):

    if board.is_checkmate():
        return -MATE
    if board.is_game_over():
        return 0
    if depth == 0:
        return evaluate_board(board)

    best_move = -float("inf")
    moves = get_ordered_moves(board)
    for move in moves:
        board.push(move)
        curr_move = min_value(depth - 1, board, alpha, beta)

        if curr_move > MATE_MAX:
            curr_move -= 1
        elif curr_move < -MATE_MAX:
            curr_move += 1
        best_move = max(
            best_move,
            curr_move,
        )
        board.pop()
        alpha = max(alpha, best_move)
        if beta <= alpha:
            return best_move
    return best_move


def min_value(depth, board, alpha, beta):

    if board.is_checkmate():
        return MATE
    if board.is_game_over():
        return 0
    if depth == 0:
        return evaluate_board(board)

    best_move = float("inf")
    moves = get_ordered_moves(board)
    for move in moves:
        board.push(move)
        curr_move = max_value(depth - 1, board, alpha, beta)
        if curr_move > MATE_MAX:
            curr_move -= 1
        elif curr_move < -MATE_MAX:
            curr_move += 1
        best_move = min(
            best_move,
            curr_move,
        )
        board.pop()
        beta = min(beta, best_move)
        if beta <= alpha:
            return best_move
    return best_move
