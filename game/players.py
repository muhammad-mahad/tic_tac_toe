"""
Player class for Tic-Tac-Toe game.
Manages player attributes and move selection.
"""
import random
from game.utils import clean_input

class Player:
    """
    Represents a player in the Tic-Tac-Toe game.
    """
    
    def __init__(self, name, marker):
        """
        Initialize a player with a name and marker (X or O).
        
        Args:
            name (str): Player's name
            marker (str): Player's marker ('X' or 'O')
        """
        self.name = name
        self.marker = marker
        # If player name is "Computer", it will make random moves
        self.is_computer = name.lower() == "computer"
    
    def get_move(self, board):
        """
        Get the player's move.
        
        If the player is a computer, a random valid move is selected.
        Otherwise, the player is prompted for input.
        
        Args:
            board (Board): The game board
            
        Returns:
            int: The selected position (1-9)
        """
        if self.is_computer:
            return self._get_computer_move(board)
        else:
            return self._get_human_move(board)
    
    def _get_human_move(self, board):
        """
        Prompt the human player for a move and validate it.
        
        Args:
            board (Board): The game board
            
        Returns:
            int: The selected position (1-9)
        """
        while True:
            try:
                position = input(f"{self.name}'s Turn ({self.marker}):\nEnter a position (1-9): ")
                position = clean_input(position)
                
                if board.is_valid_move(position):
                    return int(position)
                else:
                    print("Invalid move. Please choose an available position (1-9).")
            except ValueError:
                print("Please enter a number between 1 and 9.")
    
    def _get_computer_move(self, board):
        """
        Select a random valid move for the computer player.
        
        Args:
            board (Board): The game board
            
        Returns:
            int: The selected position (1-9)
        """
        available_moves = board.get_available_moves()
        move = random.choice(available_moves)
        print(f"{self.name}'s Turn ({self.marker}):\nComputer selects position {move}")
        return move