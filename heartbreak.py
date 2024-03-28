import turtle

s=turtle.Screen().bgcolor('black')
t=turtle.Turtle()
t.speed(3)
t.width(12)

def Curve():
    for i in range(200):
        t.right(1)
        t.forward(1)

def heart():
    t.color('red','red')
    t.begin_fill()
    t.left(140)
    t.forward(113)
    Curve()
    t.left(120)
    Curve()
    t.forward(112)
    t.end_fill()

heart()
t.pencolor('black')
t.penup()
t.goto(0,170)
t.pendown()

for broken in range(3):
    t.left(75)
    t.forward(40)
    t.right(65)
    t.forward(45)

turtle.done()