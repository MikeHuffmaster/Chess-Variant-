# Chess-Variant-
Variant of chess

# Chess Variant - MikeHuffmaster

## Overview

This program implements a variant of chess that follows the basic movement rules of a traditional chess game but excludes rules for check, checkmate, castling, en passant, and pawn promotion. The game concludes when all pieces of one type are captured, determining the winner accordingly.

## Author

- **Name:** Mike Huffmaster
- **Github:** [MikeHuffmaster](https://github.com/MikeHuffmaster)
- **Date:** 12/9/2023

## How to Play

1. Clone the repository.
2. Run the program to start a game.
3. Make moves by specifying the starting and ending points of the pieces.
4. The game ends when all pieces of one type are captured.

## Features

- Basic chess piece movement.
- Variant rules excluding check, checkmate, castling, en passant, and pawn promotion.
- Determination of the winner based on capturing all pieces of one type.

## Code Structure

The code is organized into three main classes:

1. **GameBoard:** Manages the chessboard and pieces, initializes the board, sets and gets pieces, and refreshes the board after each move.

2. **ChessVar:** Controls the gameplay, tracks players' turns, sets rules for valid moves, captures, and wins, and communicates with the GameBoard class.

3. **ChessPiece and its subclasses (Pawn, Rook, Knight, Bishop, Queen, King):** Define the attributes and movements for each type of chess piece.

##Testing

The code includes examples of testing various aspects of the game, such as normal movement, captures, turn order, and winning conditions for both black and white.

## Example testing
```python
game.make_move("e2", "e4")
game.make_move("d7", "d5")
game.show_board()
print("Game State:", game.get_game_state()
```
Feel free to explore the code and contribute to the development!

## Usage

```python
# Example usage
game = ChessVar()
game.make_move("e2", "e4")
game.make_move("e7", "e5")
game.show_board()




