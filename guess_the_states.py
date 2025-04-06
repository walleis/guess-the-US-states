import turtle
from turtle import Turtle, Screen
import pandas


# Load the GUI elements.
screen = Screen()

# Gui elements.
screen.title("Guess the U.S. States")
image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

def generate_state(x, y, state_name):
    '''Function responsible for generating the state's name on the screen. '''
    writer = Turtle()
    writer.hideturtle()
    writer.penup()
    writer.goto(x, y)
    writer.write(state_name)

# Load the state's data.
data = pandas.read_csv("./50_states.csv")
all_states = data.state.to_list()  # List of all states.
guessed_states = [] # Keeps track of all guessed states.

# Game loop.
game_is_on = True
while len(guessed_states) < 50: # While the guessed states are under 50, the game still running.
    user_answer = turtle.textinput(title=f"{len(guessed_states)}/50 Guessed states!", prompt="What's another state's name?").title()
    if user_answer == "Exit": # If the user type 'exit' the game stops.
        remaining_states = [states for states in all_states if states not in guessed_states] # Create a list of remaining states to be guessed.
        remaining_states = pandas.DataFrame(remaining_states)
        remaining_states.to_csv("remaining_states.csv")
        break

    elif user_answer in all_states and user_answer not in guessed_states:
        guessed_states.append(user_answer) # Add all the guessed states in guessed_stated.
        state_data = data[data.state == user_answer] # If the user answer is correct, it will write the guessed state in the map.
        generate_state(x= state_data.x.item(), y= state_data.y.item(), state_name= user_answer)
