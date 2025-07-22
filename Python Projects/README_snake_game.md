# Snake Game - Terminal Edition

A classic Snake game that runs in your terminal using Python and the curses library.

## Prerequisites

- Python 3.x
- windows-curses library (for Windows users)

## Installation

If you're on Windows, install the required package:
```bash
pip install windows-curses
```

## How to Run

```bash
python snake_game.py
```

## Game Controls

- **Arrow Keys**: Move the snake (Up, Down, Left, Right)
- **'q'**: Quit the game at any time

## Game Rules

1. Control the snake using arrow keys
2. Eat the food (*) to grow and increase your score
3. Avoid hitting the walls (borders) or the snake's own body
4. The game ends when the snake collides with a wall or itself
5. Your score increases by 1 for each piece of food eaten

## Features

- Real-time gameplay with smooth movement
- Score tracking
- Bordered playing field
- Game over detection
- Clean terminal interface

## Game Elements

- `#` - Snake body
- `*` - Food
- `|` and `-` - Border walls

Enjoy playing Snake in your terminal!
