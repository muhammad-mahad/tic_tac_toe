"""
Logger class for the Tic-Tac-Toe game.
Handles logging game events to files.
"""
from pathlib import Path
import time

class Logger:
    """
    Class for logging game events to files.
    """
    
    def __init__(self):
        """
        Initialize the logger and create a new game log directory.
        """
        self.log_dir = Path("game_log")
        self.log_dir.mkdir(parents=True, exist_ok=True)
        
        # Find the next game number
        game_number = self._get_next_game_number()
        
        # Create game-specific directory
        self.game_dir = self.log_dir / f"game{game_number}"
        self.game_dir.mkdir(parents=True, exist_ok=True)
        
        # Create log file
        self.log_file = self.game_dir / "log.txt"
        self.log_file.touch()
    
    def _get_next_game_number(self):
        """
        Determine the next game number by checking existing game directories.
        
        Returns:
            int: The next game number
        """
        existing_games = [d for d in self.log_dir.iterdir() if d.is_dir() and d.name.startswith("game")]
        
        if not existing_games:
            return 1
        
        # Extract numbers from directory names like "game1", "game2", etc.
        game_numbers = []
        for game_dir in existing_games:
            try:
                number = int(game_dir.name[4:])  # Remove "game" prefix
                game_numbers.append(number)
            except ValueError:
                pass
        
        return max(game_numbers, default=0) + 1
    
    def log_game_start(self, player1, player2):
        """
        Log the start of a new game.
        
        Args:
            player1 (Player): Player 1 object
            player2 (Player): Player 2 object
        """
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        header = f"Game {self._get_current_game_number()} Log\n"
        header += f"Started: {timestamp}\n\n"
        header += "Players:\n"
        header += f"- {player1.name} ({player1.marker})\n"
        header += f"- {player2.name} ({player2.marker})\n\n"
        header += f"First move: {player1.name}\n\n"
        header += "Moves:\n"
        
        with open(self.log_file, 'w') as f:
            f.write(header)
    
    def _get_current_game_number(self):
        """
        Get the current game number from the directory name.
        
        Returns:
            int: The current game number
        """
        try:
            return int(self.game_dir.name[4:])
        except ValueError:
            return 0
    
    def log_move(self, move_number, player, position, board):
        """
        Log a player's move.
        
        Args:
            move_number (int): The move number
            player (Player): The player who made the move
            position (int): The position where the move was made
            board (Board): The current board state
        """
        move_log = f"Move {move_number}: {player.name} -> Position {position}\n"
        move_log += "Board After Move:\n"
        move_log += board.get_formatted_state()
        move_log += "\n"
        
        with open(self.log_file, 'a') as f:
            f.write(move_log)
    
    def log_result(self, result):
        """
        Log the result of the game.
        
        Args:
            result (str): The result of the game (win or draw)
        """
        with open(self.log_file, 'a') as f:
            f.write(f"Result: {result}\n")
            f.write(f"Game ended: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")