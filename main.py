#!/usr/bin/env python3
"""
Main entry point for the Tic-Tac-Toe game.
Controls the overall game flow and user interactions.
"""
# Import individual modules to avoid circular imports
from game import Board
from game import Player

# Import display functions with alias for clarity
import tools.display as display_utils
from tools.logger import Logger

def main():
    """Main game loop function."""
    
    # Get player names
    player1_name = input("Please enter Player 1 name: ")
    player2_name = input("Please enter Player 2 name: ")
    
    # Welcome players using alias imports
    display_utils.display_welcome(player1_name, player2_name)
    
    play_game = True
    while play_game:
        # Initialize game components
        board = Board()
        player1 = Player(player1_name, "X")
        player2 = Player(player2_name, "O")
        current_player = player1
        
        # Create logger for this game
        logger = Logger()
        logger.log_game_start(player1, player2)
        
        # Game loop
        game_over = False
        move_count = 0
        
        while not game_over:
            # Display current board
            display_utils.display_board(board)
            
            # Get player move
            position = current_player.get_move(board)
            
            # Update board with the move
            board.place_move(position, current_player.marker)
            move_count += 1
            
            # Show marker statistics using Counter
            stats = board.get_marker_stats()
            print(f"Board stats: {stats['X']} X's, {stats['O']} O's")
            
            # Log the move
            logger.log_move(move_count, current_player, position, board)
            
            # Check for win or draw
            if board.check_winner(current_player.marker):
                display_utils.display_board(board)
                display_utils.announce_winner(current_player.name)
                logger.log_result(f"{current_player.name} wins!")
                game_over = True
            elif board.is_full():
                display_utils.display_board(board)
                print("The game ended in a draw!")
                logger.log_result("Draw")
                game_over = True
            else:
                # Switch players
                current_player = player2 if current_player == player1 else player1
        
        # Ask to play again
        play_game = display_utils.prompt_play_again()
    
    print("Thanks for playing Tic-Tac-Toe!")

if __name__ == "__main__":
    main()