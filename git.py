from turtle import *
speed(1)
bgcolor("black")
hideturtle()
setpos(0, 100)
seth(45)
penup()
pen(pencolor="#F34F29")
shape("square")
fillcolor("#F34F29")
shapesize(8, 8, 40)
stamp()
setpos(-55, 215)
pen(pencolor="black")
pendown()
seth(315)
width(18)
for i in range(2):
    forward(80)
    dot(42, "black")
backward(80)
seth(270)
forward(120)
dot(42, "black")
done()