import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"({len(guessed_states)}/50) Guess the State", prompt="Enter a State na"
                                                                                                "me").title()
    if answer_state == "Exit" or answer_state == "exit":
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        state = turtle.Turtle()
        state.penup()
        state.hideturtle()
        state.goto(float(state_data.x), float(state_data.y))
        state.write(answer_state, align="center")

# not_guessed = []
# for state in all_states:
#     if state not in guessed_states:
#         not_guessed.append(state)

not_guessed = [usa_state for usa_state in all_states if usa_state not in guessed_states]
data_dict = {
    "States": not_guessed
}
new_data = pandas.DataFrame(data_dict)
new_data.to_csv("states_missed.csv")