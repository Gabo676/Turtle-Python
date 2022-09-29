from turtle import *

from click import style

# Configuración de la ventana
wn = Screen()
wn.bgcolor("black")
wn.setup(width=450, height=500)
wn.title("Heart")

# Configuración de la flecha (tortuga)
heart = Turtle()
heart.pencolor("red")
heart.pensize(3)
heart.speed(6)

# Función para dibujar el corazón
def draw_heart():
    heart.fillcolor("red")
    heart.begin_fill()
    heart.left(140)
    heart.forward(113)
    heart.circle(-57, 200)
    heart.left(120)
    heart.circle(-57, 200)
    heart.forward(112)
    heart.end_fill()

# Función para escribir y posicionar el texto
def write_text(message, pos):
    x, y = pos
    heart.penup()
    heart.goto(x, y)
    heart.color("white")
    style = ('Script MT Bold', 30)
    heart.write(message, font=style)
    delay(150)

draw_heart()
heart.hideturtle()
write_text('I', (-80, 95))
write_text('l', (-52, 95))
write_text('o', (-45, 95))
write_text('v', (-30, 95))
write_text('e', (-14, 95))
write_text('Y', (10, 95))
write_text('o', (35, 95))
write_text('u', (50, 95))

mainloop()
