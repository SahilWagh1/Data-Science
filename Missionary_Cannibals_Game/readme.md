# Missionary and Cannibal Game

This is a console-based implementation of the Missionary and Cannibal game in Python, utilizing the `IPython.display` module to enhance the output in Jupyter Notebook or IPython environment.

## Rules of the Game

The Missionary and Cannibal game is a puzzle where the player needs to move missionaries and cannibals across a river from one bank to another, using a boat. The game follows the following rules:

- There are 3 missionaries and 3 cannibals on the left bank, along with a boat.
- The goal is to move all the missionaries and cannibals to the right bank, without violating the following conditions:
  - At any bank, the number of cannibals cannot exceed the number of missionaries, or the cannibals will eat the missionaries.
  - The boat can only carry a maximum of 2 persons (either 2 missionaries, 2 cannibals, or 1 missionary and 1 cannibal).
  - Only the player can control the boat, and the player can decide the number of missionaries and cannibals to move from one bank to another in each turn.
- The game ends in two scenarios:
  - If the player successfully moves all the missionaries and cannibals to the right bank, they win.
  - If the number of cannibals exceeds the number of missionaries on either bank, and there are missionaries remaining, the cannibals eat the missionaries, and the player loses.

## Usage

To play the game, run the Python script `Missionary_Cannibal_Game.py` in a compatible Python environment (Jupyter Notebook or IPython).

The game will display the initial state of the game, showing the number of missionaries, cannibals, and the boat's position on each bank. The player will be prompted to enter the number of missionaries and cannibals to move in each turn. The game will validate the move and update the game state accordingly.

During the game, the updated game state will be displayed using `IPython.display`, showing the number of missionaries, cannibals, and the boat's position on each bank.

Once the game ends, either by winning or losing, an appropriate message will be displayed.

## Requirements

The following dependencies are required to run the game:

- Python (version 3.5 or above)
- IPython (version 7.0 or above)

Install the required dependencies using the following command:

```shell
pip install ipython
