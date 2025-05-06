"""
Utility functions for the Tic-Tac-Toe game.
"""
from collections import Counter, deque

def clean_input(input_str):
    """
    Clean and validate user input.
    
    Args:
        input_str (str): The raw input string
        
    Returns:
        str: Cleaned input string
    """
    # Remove any whitespace and non-numeric characters
    cleaned = ''.join(char for char in input_str if char.isdigit())
    
    if not cleaned:
        raise ValueError("Input must contain at least one digit")
    
    return cleaned

def available_moves_generator(board_cells):
    """
    Generate available moves dynamically.
    
    Args:
        board_cells (list): The current board state
        
    Yields:
        int: Available position (1-9)
    """
    for i, cell in enumerate(board_cells):
        if cell not in ['X', 'O']:
            yield i + 1

# Helper functions using collections module
def create_move_history():
    """
    Create a move history deque for undo functionality.
    
    Returns:
        deque: A deque for tracking move history
    """
    return deque(maxlen=9)  # Maximum 9 moves in Tic-Tac-Toe

def count_marker_positions(board_cells):
    """
    Count occurrences of markers on the board for stats.
    
    Args:
        board_cells (list): The current board state
        
    Returns:
        Counter: Counter object with marker counts
    """
    return Counter(board_cells)