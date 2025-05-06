"""
Utility functions for the Tic-Tac-Toe game.
"""

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