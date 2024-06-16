from turtle import *

speed(3)  # Set speed

bgcolor("skyblue")

penup()
goto(-400, -100)
pendown()
color("limegreen")
begin_fill()
for i in range(2):
    forward(800)
    right(90)
    forward(400)
    right(90)
end_fill()

# gunung1
penup()
goto(-400, -100)
pendown()
color("dimgray")
begin_fill()
for i in range(3):
    forward(300)
    left(120)
end_fill()

# gunung2
penup()
goto(100, -100)
pendown()
begin_fill()
for i in range(3):
    forward(300)
    left(120)
end_fill()

# gunung3
penup()
goto(-160, -100)
pendown()
color("gray")
begin_fill()
for i in range(3):
    forward(400)
    left(120)
end_fill()

# saljuatas
penup()
goto(-35, 120)
pendown()
color("white")
begin_fill()
left(35)
forward(60)
right(90)
forward(30)
left(100)
forward(45)
right(85)
forward(65)
left(160)
forward(150)
end_fill()

# saljuatas2
penup()
goto(-215, 100)
pendown()
color("snow")
begin_fill()
forward(70)
left(120)
forward(75)
left(150)
forward(45)
right(90)
forward(45)
left(120)
end_fill()

# saljuatas3
penup()
goto(203, 80)
pendown()
begin_fill()
forward(95)
right(120)
forward(80)
right(150)
forward(50)
left(70)
end_fill()

left(50)

# matahari
penup()
goto(-500, 350)
pendown()
color("yellow")
begin_fill()
circle(125)
end_fill()

# Define fungsi pohon
def tree():
    color("saddlebrown")
    begin_fill()
    for i in range(2):
        forward(40)
        left(90)
        forward(10)
        left(90)
    end_fill()
    
    forward(10)
    left(90)
    forward(5)
    
    color("forestgreen")
    begin_fill()
    circle(25)
    end_fill()
    
    right(90)

# pohon
penup()
goto(-25,-200)
pendown()
tree()
    
penup()
goto(200,-150)
pendown()
tree()

penup()
goto(300,-250)
pendown()
tree()

penup()
goto(-300,-250)
pendown()
tree()

penup()
goto(-200,-100)
pendown()
tree()

# rumah
def drawRec(turtle, x, y, width, height, color):
    turtle.color(color)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.hideturtle()

    turtle.begin_fill()
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90) 
    turtle.forward(height)
    turtle.end_fill()

def drawTriangle(x1, y1, x2, y2, x3, y3, color):
    roof = Turtle()
    roof.hideturtle()
    roof.penup()
    roof.color(color)

    roof.goto(x1, y1)
    roof.pendown()
    roof.begin_fill()
    roof.goto(x2, y2)
    roof.goto(x3, y3)
    roof.goto(x1, y1)
    roof.end_fill()

# rumah
house = Turtle()
drawRec(house, -80, -100, 80, 95, '#ebe2af')
drawRec(house, -30, -50, 45, 20, '#a35341')
grass = Turtle()
drawRec(grass, -100, -110, 200, 10, '#b1ed7d')

window_left = Turtle()
drawRec(window_left, -70, -35, 20, 20, '#afe0d6')
window_right = Turtle()
drawRec(window_right, -30, -35, 20, 20, '#afe0d6')

window_lowerTop = Turtle()
drawRec(window_lowerTop, -70, -70, 20, 20, '#afe0d6')

window_lowerBottom = Turtle()
drawRec(window_lowerBottom, -70, -90, 20, 20, '#afe0d6')

drawTriangle(-90, -5, 10, -5, -40, 40, '#a35341')

done()