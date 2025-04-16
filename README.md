# U.S. States Guessing Game

## Description

This Python game challenges you to guess the names of the 50 U.S. states by typing them into a text input. The game displays a blank map of the United States, and when you correctly guess a state, its name will appear on the map in the correct location. The game keeps track of your correct guesses and continues until you have guessed all 50 states or choose to exit. Upon exiting, a CSV file (`remaining_states.csv`) will be generated containing the names of the states you did not guess.

## How to Play

1.  **Run the script:** Execute the Python script. A window will appear displaying a blank map of the United States with the title "Guess the U.S. States".
2.  **Enter state names:** A text input dialog will prompt you with "What's another state's name?". Type the name of a U.S. state and press Enter. The input is case-insensitive and will be automatically capitalized.
3.  **Check your guess:**
    * If your guess is a valid U.S. state and you haven't guessed it before, the state's name will be written on the map in its approximate location, and the game title will update to show the number of states you have correctly guessed.
    * If your guess is incorrect or a state you have already guessed, the game will prompt you for another state.
4.  **Exit the game:** At any point, you can type "Exit" (case-insensitive) in the text input prompt and press Enter to end the game.
5.  **View remaining states:** If you exit the game before guessing all 50 states, a file named `remaining_states.csv` will be created in the same directory as the script. This file will contain a list of the U.S. states that you did not guess.

## Functionality

* **GUI with Map:** Uses the `turtle` graphics library to display a blank map of the United States (`blank_states_img.gif`).
* **State Data:** Loads state information (names and coordinates on the map) from a CSV file named `50_states.csv` using the `pandas` library.
* **User Input:** Prompts the user to enter the names of U.S. states using `turtle.textinput()`.
* **Guess Tracking:** Keeps track of the states that have been correctly guessed and prevents повторные guesses.
* **State Name Generation:** When a correct state name is entered, a new `turtle` object is used to write the state's name at its corresponding coordinates on the map.
* **Game Termination:** The game continues until all 50 states are guessed or the user types "Exit".
* **Remaining States Output:** If the user exits before guessing all states, a CSV file named `remaining_states.csv` is created, containing the list of un-guessed states.

## Requirements

* Python 3.x
* `turtle` module (typically included with standard Python installations)
* `pandas` library (can be installed via pip: `pip install pandas`)
* Two data files in the same directory as the script:
    * `blank_states_img.gif`: An image file of a blank U.S. map.
    * `50_states.csv`: A CSV file containing the names of the 50 U.S. states and their corresponding x and y coordinates on the map image. The CSV should have columns named "state", "x", and "y".

## Installation

1.  Ensure you have Python installed on your system.
2.  Install the `pandas` library if it's not already installed:
    ```bash
    pip install pandas
    ```
3.  Download the `blank_states_img.gif` and `50_states.csv` files and place them in the same directory where you will save the Python script. You can likely find these files in the resources associated with the course or project where this code originated.
4.  Save the provided code as a `.py` file (e.g., `guess_states.py`).
5.  Run the script using a Python interpreter:
    ```bash
    python guess_states.py
    ```

## Code Explanation

* **`import turtle` and `from turtle import Turtle, Screen`:** Imports the necessary modules from the `turtle` graphics library.
* **`import pandas`:** Imports the `pandas` library for data manipulation, specifically reading the CSV file.
* **`screen = Screen()`:** Creates the main screen object for the game.
* **`screen.title("Guess the U.S. States")`:** Sets the title of the game window.
* **`image = "./blank_states_img.gif"`:** Specifies the path to the image file of the blank U.S. map.
* **`screen.addshape(image)`:** Registers the image as a new shape that can be used for turtles.
* **`turtle.shape(image)`:** Creates a turtle object and sets its shape to the loaded map image.
* **`def generate_state(x, y, state_name):`:** A function that takes x and y coordinates and a state name as input. It creates a new hidden turtle, moves it to the specified coordinates, and writes the state name on the screen.
* **`data = pandas.read_csv("./50_states.csv")`:** Reads the data from the `50_states.csv` file into a pandas DataFrame.
* **`all_states = data.state.to_list()`:** Creates a Python list containing the names of all the states from the "state" column of the DataFrame.
* **`guessed_states = []`:** An empty list to store the names of the states that the user has correctly guessed.
* **`game_is_on = True`:** A boolean flag to control the main game loop.
* **`while len(guessed_states) < 50:`:** The main game loop continues as long as the number of correctly guessed states is less than 50.
    * **`user_answer = turtle.textinput(...)`:** Prompts the user to enter a state name. `.title()` capitalizes the input.
    * **`if user_answer == "Exit":`:** If the user enters "Exit", the game loop breaks. A list of remaining states is created using a list comprehension, converted to a pandas DataFrame, and saved to `remaining_states.csv`.
    * **`elif user_answer in all_states and user_answer not in guessed_states:`:** Checks if the user's answer is a valid state name from the data and if it hasn't been guessed before.
        * **`guessed_states.append(user_answer)`:** If the guess is correct and new, the state name is added to the `guessed_states` list.
        * **`state_data = data[data.state == user_answer]`:** Retrieves the row from the DataFrame corresponding to the guessed state.
        * **`generate_state(...)`:** Calls the `generate_state` function to write the state's name at its coordinates on the map using the `.item()` method to extract the single value from the pandas Series.
* **`screen.exitonclick()`:** Keeps the game window open until the user clicks on it.
