# from turtle import Turtle, Screen


# def move_forwards():
#     tim.forward(10)


# def move_backwards():
#     tim.back(10)


# def move_ccw():
#     tim.left(10)


# def move_cw():
#     tim.right(10)


# tim = Turtle()
# my_screen = Screen()
# my_screen.listen()
# my_screen.onkey(key="w", fun=move_forwards)
# my_screen.onkey(key="s", fun=move_backwards)
# my_screen.onkey(key="a", fun=move_ccw)
# my_screen.onkey(key="d", fun=move_cw)
# my_screen.onkey(key="c", fun=tim.reset)
# my_screen.exitonclick()


from turtle import Turtle, Screen
import random


def p_instance(papa, xpos, ypos, color):
    papa.color(color)
    papa.shape("turtle")
    papa.shapesize(3, 3, 3)
    papa.penup()
    papa.setx(xpos)
    papa.sety(ypos)
    papa.pendown()


def p_pace(p_turtle, distance):
    p_turtle.forward(distance)




horizontal = -810
finish_line = 780
clergy_screen = Screen()
papa_nihil = Turtle()
p_instance(papa_nihil, horizontal, 250, "black")
print(papa_nihil.heading())

# papa1 = Turtle()
# p_instance(papa1, horizontal, 125, "steelblue3")
# #
# papa2 = Turtle()
# p_instance(papa2, horizontal, 0, "goldenrod1")
#
# papa3 = Turtle()
# p_instance(papa3, horizontal, -125, "peru")
#
# cardi_c = Turtle()
# p_instance(cardi_c, horizontal, -250, "DarkRed")

clergy_screen.exitonclick()