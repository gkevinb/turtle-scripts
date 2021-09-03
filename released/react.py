from turtle import *

speed(1)
bgcolor("black")
pen(pencolor="cyan")
shape("circle")
fillcolor("")
shapesize(15, 5, 10)
seth(90)

for i in [1, -1]:
    stamp()
    seth(i * 150)
dot(50, "cyan")
done()

# React logo, released on social media