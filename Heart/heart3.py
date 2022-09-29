from curses import window
from tkinter import *
import turtle
from math import sin, cos, pi

window = turtle.Screen()
window.title("Heart")
window.bgcolor("#f4e9cd")
window.setup(width=800, height=600)

def draw_heart(w, h, iteration=0):
    color = ['#468189', '#77aca2', '#9dbebb']

    if iteration == 3:
        return
    
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.pensize(2)

    a = 0
    t.up()
    t.fillcolor(color[iteration])
    t.begin_fill()

    while a < 2 * pi:
        x = (20 * sin(a) ** 3) * w
        y = (16 * cos(a) - 5 * cos(2 * a) - 2 * cos(3 * a) - 2*cos(4 * a)) * h
        t.goto(x, y)
        a+=0.05
        t.down()
    t.end_fill()
    draw_heart(w - 3, h - 3, iteration + 1)

    t.up()
    t.setpos(0, 0)
    t.color("white")
    t.write("Saquen plan para hoy 😏🤙", align="center", font=("Script MT Bold", 25))
    t.down()

draw_heart(18, 15)
mainloop()