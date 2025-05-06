"""
Board class for Tic-Tac-Toe game.
Handles the board state and game logic.
"""
from game.utils import available_moves_generator

class Board:
    """
    Represents the Tic-Tac-Toe game board.
    """
    
    def __init__(self):
        """Initialize an empty 3x3 board."""
        # Board is represented as a list of 9 elements (positions 1-9)
        # with values None (empty), 'X', or 'O'
        self.cells = [str(i) for i in range(1, 10)]
        
    def get_board_state(self):
        """Return the current state of the board."""
        return self.cells
    
    def is_valid_move(self, position):
        """Check if a move to the given position is valid."""
        try:
            position = int(position)
            # Check if position is in range 1-9 and not already taken
            return 1 <= position <= 9 and self.cells[position-1] not in ['X', 'O']
        except ValueError:
            return False
    
    def place_move(self, position, marker):
        """Place a marker (X or O) at the specified position."""
        if not self.is_valid_move(position):
            raise ValueError(f"Invalid move: {position}")
        
        self.cells[int(position) - 1] = marker
    
    def get_available_moves(self):
        """Return a list of available positions on the board."""
        return [i+1 for i, cell in enumerate(self.cells) if cell not in ['X', 'O']]
    
    def available_moves_gen(self):
        """Return a generator of available positions."""
        return available_moves_generator(self.cells)
    
    def is_full(self):
        """Check if the board is full (no more moves available)."""
        return all(cell in ['X', 'O'] for cell in self.cells)
    
    def check_winner(self, marker):
        """
        Check if the given marker has won the game.
        Returns True if the marker has won, False otherwise.
        """
        # Define winning combinations: rows, columns, diagonals
        win_combinations = [
            # Rows
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            # Columns
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            # Diagonals
            [0, 4, 8], [2, 4, 6]
        ]
        
        # Check each winning combination
        for combo in win_combinations:
            if all(self.cells[i] == marker for i in combo):
                return True
        
        return False
    
    def get_formatted_state(self):
        """Return the board as a formatted string for display."""
        board_str = ""
        for i in range(0, 9, 3):
            board_str += f" {self.cells[i]} | {self.cells[i+1]} | {self.cells[i+2]} \n"
            if i < 6:  # Don't add separator after the last row
                board_str += "-----------\n"
        return board_str