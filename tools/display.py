"""
Display utilities for the Tic-Tac-Toe game.
Handles all user interface elements and formatting.
"""

def display_welcome(player1_name, player2_name):
    """
    Display a welcome message for the players.
    
    Args:
        player1_name (str): Name of player 1
        player2_name (str): Name of player 2
    """
    print(f"\nWelcome, {player1_name} and {player2_name}!")

def print_board_positions():
    """
    Print a sample board showing position numbers.
    """
    print(" 1 | 2 | 3 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 7 | 8 | 9 ")

def display_board(board):
    """
    Display the current state of the board.
    
    Args:
        board (Board): The game board object
    """
    print("\nCurrent Board:")
    print(board.get_formatted_state())

def announce_winner(player_name):
    """
    Announce the winner of the game.
    
    Args:
        player_name (str): Name of the winning player
    """
    print(f"\nCongratulations, {player_name}! You win!")

def prompt_play_again():
    """
    Ask the user if they want to play another game.
    
    Returns:
        bool: True if the user wants to play again, False otherwise
    """
    while True:
        response = input("\nWould you like to play again? (yes/no): ").lower().strip()
        if response in ['yes', 'y']:
            print("\nStarting a new game...\n")
            return True
        elif response in ['no', 'n']:
            return False
        else:
            print("Please answer with 'yes' or 'no'.")