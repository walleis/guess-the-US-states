Guess the U.S. States
Welcome to Guess the U.S. States, an interactive educational game built with Python! Using the turtle module for graphics and pandas for data handling, this game challenges players to name all 50 U.S. states. As you guess, the state names appear on a blank map, and the game tracks your progress. Perfect for learning U.S. geography or practicing Python programming skills!

How It Works
The game launches a window displaying a blank U.S. map.
A prompt asks you to type a state’s name.
If the guess is correct, the state’s name is written on the map at its correct coordinates.
The game continues until all 50 states are guessed or you type "Exit" to quit.
Upon exiting, a CSV file (remaining_states.csv) is generated with the states you didn’t guess.

Requirements
Python 3.x: Ensure Python is installed on your system.
turtle: Included with standard Python installations for graphics.
pandas: Used for reading state data. Install it via pip:
pip install pandas

Data Files: The game requires:
50_states.csv: A CSV file with columns state, x, and y (state names and coordinates).
blank_states_img.gif: A GIF image of a blank U.S. map (included in the project folder).

Installation
Download or clone this repository to your computer.
Ensure the required files (50_states.csv and blank_states_img.gif) are in the same directory as the script.
Verify Python is installed by running python --version or python3 --version in your terminal.
Install pandas if not already installed (see above).
Run the game by opening a terminal in the project folder and typing:
python guess_the_states.py

Features
Displays a blank U.S. map using a GIF image as the background.
Tracks progress with a counter (e.g., "5/50 Guessed States").
Writes state names at their geographic coordinates using data from a CSV file.
Saves unguessed states to remaining_states.csv when exiting.
Prevents duplicate guesses and ignores invalid inputs gracefully.

Usage Example
Run the program, and a window with a blank U.S. map appears.
A dialog box prompts: "What's another state's name?"
Type "California" → "California" appears on the map, and the counter updates to "1/50."
Continue guessing (e.g., "Texas," "Florida").
Type "Exit" to quit → A file remaining_states.csv is created with the remaining 47 states.
