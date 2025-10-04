import random
from collections import defaultdict, Counter

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


def get_computer_choice(player_history, last_player_move=None):
   
    if not player_history:
        return random.choice(['rock', 'paper', 'scissors'])
    
    # Strategy 1: Use transition patterns if we have enough data
    if last_player_move is not None and len(player_history) >= 3:
        # Build transition dictionary: what move follows each move
        transitions = defaultdict(Counter)
        for i in range(len(player_history) - 1):
            current_move = player_history[i]
            next_move = player_history[i + 1]
            transitions[current_move][next_move] += 1
        
        # If we have data for the last move
        if last_player_move in transitions and len(transitions[last_player_move]) > 0:
            # Find the most likely next move after the last move
            most_likely_next = transitions[last_player_move].most_common(1)[0][0]
            # Return the move that beats the predicted move
            return get_counter_move(most_likely_next)
    
    # Strategy 2: Use overall frequency if transition data is insufficient
    move_counts = Counter(player_history)
    total_moves = len(player_history)
    
    # Only use frequency if we have enough data (at least 3 moves)
    if total_moves >= 3:
        # Get the most frequent move
        most_frequent = move_counts.most_common(1)[0][0]
        # Return the move that beats the most frequent move
        return get_counter_move(most_frequent)
    
    # If not enough data, choose randomly
    return random.choice(['rock', 'paper', 'scissors'])


def get_counter_move(move):
   
    counters = {
        'rock': 'paper',
        'paper': 'scissors',
        'scissors': 'rock'
    }
    return counters[move]


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
   
    print("Welcome to Rock-Paper-Scissors with Learning AI!")
    print("The computer will try to predict your moves based on your patterns.")
    print("=" * 60)
    
    # Initialize scores and history
    player_wins = 0
    computer_wins = 0
    ties = 0
    player_history = []  # Track all player moves
    last_player_move = None  # Track the most recent player move
    
    while True:
        # Get player choice
        player_choice = get_player_choice()
        
        # Check if player wants to quit
        if player_choice == 'quit':
            break
            
        # Add player choice to history
        player_history.append(player_choice)
        
        # Get computer choice based on player history
        computer_choice = get_computer_choice(player_history, last_player_move)
        
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
        
        # Update last player move for next round
        last_player_move = player_choice
        
        # Add a separator for readability
        print("-" * 60)
    
    # Game ended, display final results
    print("\nGame Over!")
    print(f"Final Score - You: {player_wins} | Computer: {computer_wins} | Ties: {ties}")
    
    overall_winner = determine_overall_winner(player_wins, computer_wins)
    if overall_winner == 'player':
        print("Congratulations! You outsmarted the learning AI!")
    elif overall_winner == 'computer':
        print("The learning AI won! It adapted to your patterns.")
    else:
        print("The game ended in a tie! You and the AI were evenly matched.")


if __name__ == "__main__":
    main_game_loop()