import random
import turtle
from tkinter import simpledialog


# Returns a random color!
def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


# ====================== DO NOT EDIT THE CODE ABOVE ===========================

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # TODO 1) Create a new Turtle
    for i in range(5):
        my_turtle = turtle.Turtle()
        my_turtle.shape('turtle')
        my_turtle.speed(2)
        my_turtle.width(10)
        pen_color = simpledialog.askstring(title='Pen color', prompt='What pen color would you like?')
        if pen_color == pen_color:
            my_turtle.color(pen_color)
        if pen_color == '':
            my_turtle.color(get_random_color())
        my_turtle.circle(radius=50, steps=30)
    #      2) Make the turtle draw a shape (this will take more than one line
    #         of code)
    #      3) Set the pen width to 10
    #      4) Ask the user what color pen they would like to draw with
    #      5) Use an if/else statement to set the pen color that the user
    #         requested
    #      6) If the user doesn't enter anything, choose a random color
    #      7) Put a loop around your code so that you keep asking the user for
    #         more colors & drawing them

    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
