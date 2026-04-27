# Minimax Algorithm Implementation

This repository contains an implementation of the Minimax decision-making algorithm. The project demonstrates how artificial intelligence can determine the optimal move in a competitive, two-player zero-sum game environment by simulating all possible future game states.

## Project Overview
The Minimax algorithm works by minimizing the possible loss for a worst-case (maximum loss) scenario. In this implementation, the "Maximizer" seeks the highest possible score, while the "Minimizer" seeks the lowest possible score.

## Features
* **Recursive State Tree Exploration**: Systematically evaluates the game tree to find the optimal path.
* **Heuristic Evaluation**: Includes a scoring system to evaluate non-terminal board states.
* **Backtracking**: Efficiently passes scores up the tree to the root node to make the final move decision.

## Technical Details
* **Language**: C++ / Python (based on repository structure).
* **Game Logic**: Evaluation of game-over conditions (Win, Loss, Draw).
* **Depth Control**: Support for limited-depth searches to manage computational complexity in games with large state spaces.

## How It Works
1. **Generation**: The algorithm generates the entire tree of possible moves from the current state.
2. **Evaluation**: It applies an evaluation function to the leaf nodes (terminal states).
3. **Propagation**: 
    * If it is the Maximizer's turn, the algorithm chooses the child with the maximum score.
    * If it is the Minimizer's turn, the algorithm chooses the child with the minimum score.
4. **Decision**: The optimal move is selected based on the value propagated back to the root.

## Optimization (Alpha-Beta Pruning)
*Note: If implemented, this significantly improves performance.*
The project may include Alpha-Beta pruning to decrease the number of nodes evaluated in the search tree, allowing the algorithm to search deeper within the same time constraints by "pruning" branches that cannot possibly influence the final decision.

## Usage
1. Compile the source code using the provided build instructions or script.
2. Run the executable to observe the AI's decision-making process.
3. (Optional) Adjust the search depth or heuristic parameters to test different AI behaviors.
