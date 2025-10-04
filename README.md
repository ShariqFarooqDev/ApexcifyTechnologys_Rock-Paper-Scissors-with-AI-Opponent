# Rock Paper Scissors Game

A Python implementation of the classic Rock-Paper-Scissors game with two different AI opponents: a random AI and a learning AI that adapts to your playing patterns.

## Features

### Two Game Modes

1. **Random AI (`rps_random_ai.py`)**: A fair opponent that makes completely random choices
2. **Learning AI (`rps_learning_ai.py`)**: An intelligent opponent that learns from your move patterns and tries to predict your next move

### Game Capabilities

- Simple, intuitive command-line interface
- Score tracking across multiple rounds
- Play as many rounds as you want
- Easy-to-use input options (single letters or full words)
- Real-time feedback on each round
- Final game statistics

## Requirements

- Python 3.x
- No external dependencies (uses only standard library)

## Installation

1. Clone or download this repository
2. Ensure you have Python 3 installed on your system
3. No additional packages need to be installed

## How to Play

### Running the Random AI Version

```bash
python rps_random_ai.py
```

### Running the Learning AI Version

```bash
python rps_learning_ai.py
```

### Game Controls

When prompted, enter your choice:
- `r` or `rock` - Choose Rock
- `p` or `paper` - Choose Paper
- `s` or `scissors` - Choose Scissors
- `q` or `quit` - End the game

### Game Rules

- Rock beats Scissors
- Scissors beats Paper
- Paper beats Rock
- Same choices result in a tie

## How the Learning AI Works

The learning AI uses two strategies to predict your moves:

1. **Transition Pattern Analysis**: Tracks which moves you tend to make after specific moves (e.g., if you often play paper after rock)
2. **Frequency Analysis**: Identifies your most frequently played move and counters it

The AI needs at least 3 moves to start learning your patterns. Until then, it plays randomly.

## Gameplay Example

```
Welcome to Rock-Paper-Scissors!
================================
Choose rock (r), paper (p), scissors (s), or quit (q): r

You chose: rock
Computer chose: scissors
You win this round!

Current Score - You: 1 | Computer: 0 | Ties: 0
------------------------------
```

## Tips for Beating the Learning AI

- Vary your move patterns
- Avoid repeating sequences
- Mix up your strategy throughout the game
- Try to be as random as possible

## Code Structure

Both versions share similar structure with these key functions:

- `get_player_choice()`: Handles user input and validation
- `get_computer_choice()`: Generates the computer's move (random or learned)
- `determine_winner()`: Evaluates round outcomes
- `display_round_result()`: Shows round results
- `display_scores()`: Displays current score
- `main_game_loop()`: Controls the game flow

The learning AI version includes additional functions:
- `get_counter_move()`: Returns the move that beats a given move
- Pattern analysis using `defaultdict` and `Counter` from collections

## License

Feel free to use, modify, and distribute this code for educational and personal projects.

## Contributing

Suggestions and improvements are welcome! Feel free to fork and submit pull requests.

## Future Enhancements

Possible features for future versions:
- GUI interface
- More sophisticated learning algorithms
- Multiplayer support
- Extended game modes (Rock-Paper-Scissors-Lizard-Spock)
- Save/load game statistics
- Difficulty levels for the learning AI