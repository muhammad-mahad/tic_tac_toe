# Tic-Tac-Toe Command Line Game

A modular Python implementation of the classic Tic-Tac-Toe game, designed to run in the command line.

## Project Structure

```
tic_tac_toe/
├── main.py
├── game/
│   ├── __init__.py
│   ├── board.py
│   ├── players.py
│   └── utils.py
└── tools/
    ├── display.py
    └── logger.py
```

## Features

- Two-player game with customizable player names
- Optional computer player (use "Computer" as the player name)
- Clean modular code structure
- Game logging with persistent history
- Board visualization in the console
- Input validation and error handling

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/tic_tac_toe.git
   cd tic_tac_toe
   ```

2. Run the game:
   ```bash
   python main.py
   ```

3. Follow the on-screen instructions to play the game:
   - Enter both player names
   - Players take turns entering a position number (1-9)
   - The game automatically checks for wins or draws
   - Choose to play again or exit after a game ends

## Game Logs

Game logs are automatically saved in the `game_log` directory. Each game is stored in its own folder with a detailed log file containing:
- Player information
- Move history
- Board state after each move
- Game result

## Requirements

- Python 3.6 or higher

## Implementation Details

- The `Board` class manages the game state and checks for win/draw conditions
- The `Player` class handles player input and move selection
- Utilities include input validation and move generators
- Display functions manage the game's user interface
- Logger class creates and maintains game history logs
