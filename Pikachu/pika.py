import turtle


def getPosition(x, y):
    turtle.setx(x)
    turtle.sety(y)
    print(x, y)

class Pikachu:

    def __init__(self):
        self.t = turtle.Turtle()
        t = self.t
        t.pensize(2)
        t.speed(0)
        t.ondrag(getPosition)

    def noTrace_goto(self, x, y):
        self.t.penup()
        self.t.goto(x, y)
        self.t.pendown()

    def leftEye(self, x, y):
        self.noTrace_goto(x, y)
        t = self.t
        t.seth(0)
        t.fillcolor('#000')
        t.begin_fill()
        t.circle(27)
        t.end_fill()

        self.noTrace_goto(x+6, y + 27)
        t.fillcolor('#ffffff')
        t.begin_fill()
        t.circle(13)
        t.end_fill()

    def rightEye(self, x, y):
        self.noTrace_goto(x, y)
        t = self.t
        t.seth(0)
        t.fillcolor('#000')
        t.begin_fill()
        t.circle(27)
        t.end_fill()

        self.noTrace_goto(x-6, y + 27)
        t.fillcolor('#ffffff')
        t.begin_fill()
        t.circle(13)
        t.end_fill()

    def mouth(self, x, y):
        self.noTrace_goto(x, y)
        t = self.t
        
        # labio superior 
        t.seth(-50)
        t.color('#000000')
        t.circle(15, 60)
        t.circle(100, 20)
        t.seth(-30)
        t.circle(100, 20)
        t.circle(15, 60)

        # nariz
        self.noTrace_goto(-20, 45)
        t.seth(8)
        t.fd(15)
        t.back(8)
    
    # mejillas rojas
    def leftCheek(self, x, y):
        turtle.tracer(False)
        t = self.t
        self.noTrace_goto(x, y)
        t.seth(300)
        t.fillcolor('#ff0000')
        t.begin_fill()
        a = 2.3
        for i in range(120):
            if 0 <= i < 30 or 60 <= i < 90:
                a -= 0.05
                t.lt(3)
                t.fd(a)
            else:
                a += 0.05
                t.lt(3)
                t.fd(a)
        t.end_fill()
        turtle.tracer(True)

    def rightCheek(self, x, y):
        t = self.t
        turtle.tracer(False)
        self.noTrace_goto(x, y)
        t.seth(60)
        t.fillcolor('#ff0000')
        t.begin_fill()
        a = 2.3
        for i in range(120):
            if 0 <= i < 30 or 60 <= i < 90:
                a -= 0.05
                t.lt(3)
                t.fd(a)
            else:
                a += 0.05
                t.lt(3)
                t.fd(a)
        t.end_fill()
        turtle.tracer(True)


    def colorLeftEar(self, x, y):
        t = self.t
        self.noTrace_goto(x, y)
        t.fillcolor('#000000')
        t.begin_fill()
        t.seth(130)
        t.circle(140, 30)
        t.circle(30, 50)
        t.seth(295)
        t.circle(180, 25)
        t.end_fill()

    def colorRightEar(self, x, y):
        t = self.t
        self.noTrace_goto(x, y)
        t.fillcolor('#000000')
        t.begin_fill()
        t.seth(300)
        t.circle(-100, 30)
        t.seth(35)
        t.circle(300, 15)
        t.circle(30, 50)
        t.seth(190)
        t.circle(300, 17)
        t.end_fill()

    def body(self):
        t = self.t

        # Cola
        self.noTrace_goto(110, 100)
        t.fillcolor('#F6D02F')
        t.begin_fill()
        t.seth(40)
        t.fd(200)
        t.seth(-80)
        t.fd(150)
        t.seth(210)
        t.fd(150)
        t.left(90)
        t.fd(100)
        t.right(95)
        t.fd(100)
        t.left(110)
        t.fd(70)
        t.right(110)
        t.fd(80)
        t.left(110)
        t.fd(30)
        t.right(110)
        t.fd(32)

        t.right(106)
        t.circle(100, 25)
        t.right(15)
        t.circle(-300, 2)

        t.seth(30)
        t.fd(40)
        t.left(100)
        t.fd(70)
        t.right(100)
        t.fd(80)
        t.left(100)
        t.fd(46)
        t.seth(66)
        t.circle(200, 38)
        t.right(10)
        t.fd(10)
        t.end_fill()

        # patrón de cola
        t.fillcolor('#923E24')
        self.noTrace_goto(68, -190)
        t.begin_fill()
        
        t.seth(30)
        t.fd(40)
        t.left(100)
        t.fd(40)
        t.pencolor('#923e24')
        t.seth(-30)
        t.fd(30)
        t.left(140)
        t.fd(20)
        t.right(150)
        t.fd(20)
        t.left(150)
        t.fd(20)
        t.right(150)
        t.fd(20)
        t.left(130)
        t.fd(18)
        t.pencolor('#000000')
        t.seth(-45)
        t.fd(67)
        t.right(110)
        t.fd(80)
        t.left(110)
        t.fd(30)
        t.right(110)
        t.fd(32)
        t.right(106)
        t.circle(100, 25)
        t.right(15)
        t.circle(-300, 2)
        t.end_fill()

        self.noTrace_goto(35, -90)
        t.fillcolor('#F6D02F')
        t.begin_fill()
        # contorno de la cara derecha
        t.seth(20)
        t.forward(30)
        t.circle(100, 90)
        t.circle(-30, 20)
        t.left(-10)
        t.circle(160, 30)
        t.circle(30, 50)

        # oreja derecha
        t.seth(20)
        t.circle(300, 30)
        t.circle(30, 50)
        t.seth(190)
        t.circle(300, 35)

        # contorno superior
        t.seth(150)
        t.circle(200, 60)
        
        # oreja izquierda
        t.seth(120)
        t.circle(300, 30)
        t.circle(30, 50)
        t.seth(295)
        t.circle(300, 35)
        #print(t.pos())

        # contorno de la cara izquierda
        t.seth(210)
        t.circle(30, 50)
        t.seth(250)
        t.circle(160, 30)
        t.left(-10)
        t.circle(-30, 20)
        t.circle(100, 90)
        t.forward(40)

        #Cuepor izquierdo
        t.penup()
        t.forward(-63)
        t.left(90)
        t.forward(2)
        t.seth(75)
        t.pendown()
        t.circle(300, -8)
        t.left(180)
        t.circle(-300, 15)
        t.seth(240)
        t.circle(100, 45)

        # pie izquierdo
        t.seth(0)
        t.left(130)
        t.penup()
        t.forward(-20)
        t.pendown()
        t.circle(130, 20)
        t.circle(5, 155)
        t.forward(30)

    
        t.forward(-30)
        t.seth(90)
        t.circle(5, 215)
        t.forward(25)

        t.forward(-20)
        t.seth(80)
        t.circle(3, 215)
        t.circle(160, 40)

        t.circle(10, 150)

        # contorno inferior
        self.noTrace_goto(125, -240)
        t.penup()
        t.seth(0)
        t.forward(-265)
        t.seth(90)
        t.forward(-76)
        t.seth(0)
        t.pendown()
        t.circle(150, 10)
        t.seth(0)
        t.penup()
        t.forward(63)
        t.seth(90)
        t.forward(10)
        t.pendown()
        t.seth(0)
        t.circle(-350, 10)

        t.penup()
        t.seth(0)
        t.forward(50)
        t.seth(90)
        t.forward(-10)
        t.pendown()
        t.seth(335)
        t.circle(280, 9)

        self.noTrace_goto(100, -230)
        # pie derecho
        t.penup()
        t.seth(90)
        t.forward(-100)
        t.pendown()
        t.seth(-90)
        t.circle(10, 150)
        t.seth(45)
        t.circle(160, 40)


        t.circle(3, 160)
        t.forward(25)
        t.forward(-30)
        t.seth(90)
        t.circle(5, 150)
        t.forward(20)
        t.forward(-18)
        t.seth(90)
        t.circle(5, 150)
        t.seth(0)
        t.left(225)
        t.circle(130, 20)

        self.noTrace_goto(125, -250)
        # cuerpo derecho
        t.seth(80)
        t.circle(150, 30)
        t.seth(120)
        t.circle(-400, 16)

        t.end_fill()

        self.noTrace_goto(5, -125)
        # Mano derecha
        t.fillcolor('#F6D02F')
        t.begin_fill()
        t.seth(0)
        #t.pendown()
        t.seth(255)
        t.circle(320, 38)

        t.seth(70)
        t.forward(10)
        t.seth(280)
        t.forward(10)
        t.seth(45)
        t.forward(10)
        t.seth(280)
        t.forward(10)
        t.seth(45)
        t.forward(10)
        t.seth(280)
        t.forward(10)
        t.seth(50)
        t.forward(10)
        t.seth(340)
        t.forward(10)
        t.seth(110)
        t.forward(10)
        t.seth(55)
        t.circle(258, 25)

        t.end_fill()

        self.noTrace_goto(-130, -230)
        # mano izquierda
        t.fillcolor('#F6D02F')
        t.begin_fill()
        t.seth(270)
        t.circle(220, 25)
        t.left(320)
        t.forward(10)
        t.seth(0)
        t.circle(20, 45)
        t.seth(280)
        t.forward(10)
        t.seth(45)
        t.forward(10)
        t.seth(280)
        t.forward(10)
        t.seth(45)
        t.forward(10)
        t.seth(280)
        t.forward(10)
        t.seth(50)
        t.forward(15)
        t.seth(280)
        t.forward(10)
        t.seth(50)
        t.forward(10)
        t.seth(70)
        t.circle(320, 38)
        t.end_fill()

        #ojos, boca, mejillas
        self.mouth(-60, 15)
        self.leftCheek(-163, -20)
        self.rightCheek(125, -18)
        self.colorLeftEar(-185, 258)
        self.colorRightEar(150, 245)
        self.leftEye(-115, 55)
        self.rightEye(75, 55)
        t.hideturtle()


    def start(self):
        self.body()



def main():
    turtle.setup(1200, 720)
    turtle.title('Pikachu')
    pikachu = Pikachu()
    pikachu.start()
    turtle.mainloop()

if __name__ == '__main__':
    main()