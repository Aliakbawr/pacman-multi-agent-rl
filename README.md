## Project Structure

- **multiAgents.py**: The main script that implements the Pacman and ghost agents using Q-learning, Minimax, and Alpha-beta pruning.
- **util.py**: Utility functions and classes used throughout the project.
- **pacman.py**: Contains the game logic for Pacman.
- **game.py**: Defines the core framework for the Pacman game.
- **requirements.txt**: Lists the required Python packages for the project.

## Installation

**Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/pacman-multi-agent-rl.git
    cd pacman-multi-agent-rl
    ```
## Dependencies

- `numpy`: For numerical operations.
- `matplotlib`: For plotting (if required).
- `pygame`: For rendering the game environment.

Install dependencies with:
```sh
pip install numpy matplotlib pygame
```

## Usage

Run the main script to start the Pacman game with AI agents:
```sh
python multiAgents.py
```

The script performs the following steps:

1. **Game Initialization**:
    ```python
    from game import GameState
    ```

2. **Agent Definition**:
    - **Pacman Agent**: Uses Minimax and Alpha-beta pruning algorithms.
    - **Ghost Agents**: Can also use various strategies for decision making.

3. **Algorithm Implementation**:
    - **Minimax Algorithm**:
        ```python
        def maxValue(self, gameState: GameState, depth, agentIndex, alpha, beta):
            # Implementation of the max value function for Minimax
        ```

    - **Alpha-beta Pruning**:
        ```python
        def minValue(self, gameState: GameState, depth, agentIndex, alpha, beta):
            # Implementation of the min value function with alpha-beta pruning
        ```

4. **Action Selection**:
    The best action for Pacman is selected using the evaluated scores from the Minimax algorithm.
    ```python
    def getAction(self, gameState: GameState):
        # Implementation of the action selection process
    ```

## Evaluation Function

The evaluation function scores the current game state for Pacman based on several factors such as the distance to the nearest ghost and food, and the number of food pellets remaining:
```python
def scoreEvaluationFunction(currentGameState: GameState):
    # Implementation of the evaluation function
```

## Algorithms

### Q-learning

Q-learning is an off-policy TD control algorithm used to find the best action to take given the current state.

### Minimax

Minimax is a recursive algorithm used for choosing the next move in two-player games. In Pacman, this involves looking ahead to future moves to minimize the possible loss.

### Alpha-beta Pruning

Alpha-beta pruning is an optimization technique for the Minimax algorithm that reduces the number of nodes evaluated by the minimax algorithm in its search tree.

## Acknowledgements

The Pacman AI projects were developed at UC Berkeley. The core projects and autograders were primarily created by John DeNero and Dan Klein. Student side autograding was added by Brad Miller, Nick Hay, and Pieter Abbeel.

For more details, visit [UC Berkeley's AI course](http://ai.berkeley.edu).

---

Feel free to reach out for any questions or contributions to improve the project!
