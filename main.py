import turtle
import pandas

screen = turtle.Screen()
tim = turtle.Turtle()
image = "blank_states_img.gif"
screen.addshape(image)
# this adds specified shape to our turtle module

turtle.shape(image)


# def get_click_locations(x, y)
    # print(x,y)
# screen.onscreenclick(get_click_locations)
# this screen method tracks the x,y location where a user clicks with a mouse on screen
# and passes that x,y to a function specified
data = pandas.read_csv("50_states.csv")


list_of_states = data["state"].to_list()

def write_on_map(state):
    x = data[data["state"] == state].x.item()
    y = data[data["state"] == state].y.item()

    # series.item() fetches only actual value of the series removing its index

    tim.hideturtle()
    tim.penup()
    tim.goto(x, y)
    tim.write(arg=state, align='left', font=('Arial', 8, 'normal'))

def update_score(score):
    score += 1
    return score

score = 0
guessed_state = []
guess_is_on = True

while guess_is_on:
    user_input = screen.textinput(title=f"{score}/50 corectly guessed.", prompt="Give any of US states name:").title()
    # changes to title case i.e. first letterr capital

    for state in list_of_states:

        if user_input == state:
           write_on_map(state)
           score = update_score(score)
           guessed_state.append(state)
           if score == 50:
               guess_is_on = False
        else:
            pass

    if user_input == "Exit":
        break

not_guessed_states = [states for states in list_of_states if states not in guessed_state]

dict = {"state":not_guessed_states}

pandas.DataFrame(dict).to_csv("not_guessed_states.csv")








