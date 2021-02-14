import turtle
import pandas

data = pandas.read_csv("50_states.csv")
image = "blank_states_img.gif"
screen = turtle.Screen()
screen.title("U.S States Game")
# Add bg image to turtle
screen.addshape(image)
turtle.shape(image)
correct_answer_count = 0
guessed_states = []
all_states = data.state.to_list()


def user_prompt():
    answer_state = screen.textinput(title=f"{correct_answer_count}/50 States Correct",
                                    prompt="What's anther state's name?").title()

    return answer_state


while len(guessed_states) < 50:

    user_answer = user_prompt()

    if user_answer == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if user_answer in all_states:
        guessed_states.append(user_answer)
        correct_answer_count += 1
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        row = data[data.state == user_answer]
        t.goto(int(row.x), int(row.y))
        t.write(user_answer)

screen.exitonclick()
