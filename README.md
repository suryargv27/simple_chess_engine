# Simple Chess Engine

## Overview
This is a simple chess engine written in Python using the `python-chess` library. The engine evaluates board positions using piece-square tables and basic material evaluation, and it searches for optimal moves using the minimax algorithm with alpha-beta pruning.

## Features
- Supports legal move generation
- Evaluates board positions based on material and positional values
- Uses alpha-beta pruning to optimize search depth
- Allows human vs. AI play
- Displays board using Unicode chess symbols

## Installation
```bash
pip install chess
```

## How to Play
Run the `main.py` file and choose whether to play as white or black:
```bash
python main.py
```
Enter your moves using standard chess notation (e.g., `e2e4`).

## Algorithm
The chess engine evaluates board positions using the following formula:

$$
E = \sum_{i} \left( V(p_i) + P(p_i, s_i) \right)
$$

Where:
- $E$ is the total evaluation score.
- $V(p_i)$ is the material value of piece $p_i$.
- $P(p_i, s_i)$ is the positional value of piece $p_i$ on square $s_i$.

Material values are defined as:
- Pawn: $100$
- Knight: $320$
- Bishop: $330$
- Rook: $500$
- Queen: $900$
- King: $20000$

Each piece has a predefined positional evaluation table that adjusts its score based on its position.

## Minimax Algorithm with Alpha-Beta Pruning
The engine searches for the best move using a depth-limited minimax algorithm with alpha-beta pruning:

1. Generate all legal moves.
2. Evaluate the resulting board positions using the evaluation function.
3. Recursively apply the minimax algorithm to explore deeper moves.
4. Use alpha-beta pruning to eliminate unnecessary branches and improve efficiency.

The minimax formula is:

$$
V(s, d) = \begin{cases} \max_{a \in A(s)} V(s', d-1) & \text{if maximizing player} \\ \min_{a \in A(s)} V(s', d-1) & \text{if minimizing player} \end{cases}
$$

Where:
- $V(s, d)$ is the evaluation score at state $s$ and depth $d$.
- $A(s)$ is the set of available actions from state $s$.
- $s'$ is the resulting state after taking action $a$.

Alpha-beta pruning ensures that unnecessary branches are cut off when:
- $\alpha \geq \beta$
- $\alpha = \max(\alpha, V(s', d-1))$ for the maximizing player
- $\beta = \min(\beta, V(s', d-1))$ for the minimizing player

## File Structure
```
chess-engine/
├── evaluate.py       # Board evaluation logic
├── movegeneration.py # Move generation and minimax implementation
├── main.py           # Main game loop
├── README.md         # Project documentation
```

## Future Improvements
- Implement transposition tables for better performance
- Add support for different search heuristics (e.g., iterative deepening, Monte Carlo Tree Search)
- Improve positional evaluation with neural networks

## License
This project is open-source and available under the MIT License.

