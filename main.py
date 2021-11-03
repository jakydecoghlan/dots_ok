# import colorgram
import turtle as t
import random

# colors = colorgram.extract('Damien_Hirst_polkadots.jpg', 30)
# rgb_colors = []
# first_color = colors[0].rgb

# print(first_color)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
rgb_colors = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

def random_color():
    color = random.choice(rgb_colors)
    return color

donatello = t.Turtle()
screen = t.Screen()

screen.colormode(255)
donatello.shape("turtle")
donatello.speed("fastest")
donatello.penup()

def linea_de_puntos(puntos_x):
    for i in range(puntos_x):
        donatello.dot(20, random_color())
        donatello.forward(50)

# donatello.setposition(-250, -300)

def hirst_dots(initial_x, initial_y, puntos_x, puntos_y):
    donatello.setposition(initial_x, initial_y)
    eje_y = initial_y
    for i in range(puntos_y):
        linea_de_puntos(puntos_x)
        eje_y += 50
        donatello.setposition(initial_x, eje_y)

donatello.hideturtle()
hirst_dots(-250, -300, 10, 50)

print(tp)


screen.exitonclick()