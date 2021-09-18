from turtle import *

speed(100)
bgcolor("black")
pen(pencolor="#80b602")
shape("square")
fillcolor("#80b602")
penup()
width(1)
seth(90)
forward(30)
shapesize(6, 5, 40)

stamp()

shapesize(6, 6, 40)


shape("circle")
# seth(90)
forward(55)
stamp()

hideturtle()

def limb(x, y):
    goto(x, y)
    pendown()
    width(40)
    forward(70)
    penup()

limb(108, 0)
limb(-108, 0)
limb(33, -80)
limb(-33, -80)

goto(35, 128)
dot(14, "black")
goto(-35, 128)
dot(14, "black")

def antenna(x, y, angle):
    goto(x, y)
    width(5)
    pendown()
    seth(angle)
    forward(35)
    penup()

antenna(30, 150, 65)
antenna(-30, 150, 115)

penup()

goto(80, 90)
pen(pencolor="black")
width(8)
pendown()
seth(0)
back(160)

done()