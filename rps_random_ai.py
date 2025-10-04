import random

def get_player_choice():
   
    # Mapping from abbreviations to full names
    choice_map = {
        'r': 'rock',
        'p': 'paper',
        's': 'scissors'
    }
    
    while True:
        raw_input = input("Choose rock (r), paper (p), scissors (s), or quit (q): ").lower().strip()
        
        # Handle quit
        if raw_input in ['quit', 'q']:
            return 'quit'
        
        # Handle single-letter input
        if raw_input in choice_map:
            return choice_map[raw_input]
        
        # Handle full-word input
        if raw_input in ['rock', 'paper', 'scissors']:
            return raw_input
        
        # Invalid input
        print("Invalid choice. Please enter 'r', 'p', 's', or 'quit'.")


def get_computer_choice():
  
    return random.choice(['rock', 'paper', 'scissors'])


def determine_winner(player_choice, computer_choice):
    
    if player_choice == computer_choice:
        return 'tie'
    
    # Define winning combinations
    win_conditions = {
        'rock': 'scissors',
        'scissors': 'paper',
        'paper': 'rock'
    }
    
    if win_conditions[player_choice] == computer_choice:
        return 'player'
    else:
        return 'computer'


def display_round_result(player_choice, computer_choice, winner):
   
    print(f"\nYou chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")
    
    if winner == 'tie':
        print("It's a tie!")
    elif winner == 'player':
        print("You win this round!")
    else:
        print("Computer wins this round!")


def display_scores(player_wins, computer_wins, ties):
   
    print(f"\nCurrent Score - You: {player_wins} | Computer: {computer_wins} | Ties: {ties}")


def determine_overall_winner(player_wins, computer_wins):
   
    if player_wins > computer_wins:
        return 'player'
    elif computer_wins > player_wins:
        return 'computer'
    else:
        return 'tie'


def main_game_loop():
   
    print("Welcome to Rock-Paper-Scissors!")
    print("================================")
    
    # Initialize scores
    player_wins = 0
    computer_wins = 0
    ties = 0
    
    while True:
        # Get player choice
        player_choice = get_player_choice()
        
        # Check if player wants to quit
        if player_choice == 'quit':
            break
            
        # Get computer choice
        computer_choice = get_computer_choice()
        
        # Determine winner
        winner = determine_winner(player_choice, computer_choice)
        
        # Update scores
        if winner == 'player':
            player_wins += 1
        elif winner == 'computer':
            computer_wins += 1
        else:
            ties += 1
            
        # Display round result
        display_round_result(player_choice, computer_choice, winner)
        
        # Display current scores
        display_scores(player_wins, computer_wins, ties)
        
        # Add a separator for readability
        print("-" * 30)
    
    # Game ended, display final results
    print("\nGame Over!")
    print(f"Final Score - You: {player_wins} | Computer: {computer_wins} | Ties: {ties}")
    
    overall_winner = determine_overall_winner(player_wins, computer_wins)
    if overall_winner == 'player':
        print("Congratulations! You won the game!")
    elif overall_winner == 'computer':
        print("Computer won the game. Better luck next time!")
    else:
        print("The game ended in a tie!")


if __name__ == "__main__":
    main_game_loop()