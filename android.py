from turtle import *

speed(1)
bgcolor("black")
pen(pencolor="#80b602")
shape("square")
fillcolor("#80b602")
penup()
width(1)
shapesize(6, 6, 40)
# shapesize(5, 6, 40)
stamp()


shape("circle")
seth(90)
forward(65)
stamp()

hideturtle()

def limb(x, y):
    goto(x, y)
    pendown()
    width(40)
    forward(80)
    penup()

limb(110, -30)
limb(-110, -30)
limb(33, -120)
limb(-33, -120)

goto(35, 106)
dot(14, "black")
goto(-35, 106)
dot(14, "black")

def antenna(x, y, angle):
    goto(x, y)
    width(5)
    pendown()
    seth(angle)
    forward(35)
    penup()

antenna(35, 130, 65)
antenna(-35, 130, 115)

penup()

goto(80, 70)
pen(pencolor="black")
width(8)
pendown()
seth(0)
back(160)

done()