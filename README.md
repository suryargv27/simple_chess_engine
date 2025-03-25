# Simple Chess Engine

## Overview
This is a simple chess engine implemented in Python using the `python-chess` library. It features basic move evaluation based on piece values and positional heuristics. The engine allows a user to play against the AI, which evaluates moves using a scoring function.

## Features
- Supports legal chess moves using `python-chess`.
- Evaluates board position based on piece-square tables and piece values.
- Implements an AI that selects moves based on a heuristic evaluation function.
- Interactive CLI-based gameplay.
- Supports different game phases (opening, midgame, and endgame) for accurate evaluation.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/simple-chess-engine.git
   cd simple-chess-engine
   ```
2. Install dependencies:
   ```sh
   pip install python-chess
   ```

## Usage

Run the game using:
```sh
python main.py
```
You will be prompted to select your side (White or Black) and enter moves in algebraic notation (e.g., `e2e4`). The AI will respond based on its evaluation function.

## File Structure
```
├── evaluate.py        # Contains evaluation logic for board positions
├── movegeneration.py  # Implements AI move generation
├── main.py            # Runs the game and handles user input
└── README.md          # Documentation
```

## Evaluation Function
The engine evaluates moves based on:
1. **Piece Value:** Each piece has a predefined static value:
   - Pawn: \(100\)
   - Knight: \(320\)
   - Bishop: \(330\)
   - Rook: \(500\)
   - Queen: \(900\)
   - King: \(20000\)

2. **Positional Heuristics:** Each piece has a position-based evaluation table (piece-square tables) to favor good positions.
3. **Captures:** Moves that capture higher-value pieces are favored.
4. **Endgame Heuristics:** Different evaluation for king positioning in the endgame.

### Move Evaluation Formula
For a given move \(m\), the evaluation function is:
\[
V(m) = V_{capture} + (V_{to} - V_{from})
\]
where:
- \(V_{capture}\) is the value of the captured piece (if any).
- \(V_{to}\) and \(V_{from}\) are the positional values before and after the move.

If the move is a promotion, it gets a high positive score.

## Example Game
```
Start as [w]hite or [b]lack:
w
  8 ♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜
  7 ♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟
  6 · · · · · · · ·
  5 · · · · · · · ·
  4 · · · · · · · ·
  3 · · · · · · · ·
  2 ♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙
  1 ♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖
    a b c d e f g h

Your move:
e2e4
...
```

## Future Improvements
- Implementing Minimax with Alpha-Beta pruning.
- Adding a more sophisticated evaluation function.
- Enhancing AI difficulty levels.

## License
This project is open-source and licensed under the MIT License.

