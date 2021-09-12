from turtle import *
bgcolor("black")
seth(90)
forward(100)
dot(260, "#FF4500")
pen(pencolor="white")
hideturtle()

shape("circle")
fillcolor("white")
backward(30)
shapesize(7, 4.7, 12)
stamp()

penup()

# ears
shapesize(2, 2, 2)
setpos(-68, 90)
stamp()
setpos(68, 90)
stamp()


# antenna
setpos(0, 90)
pendown()
pensize(8)
setpos(15, 165)
setpos(58, 155)

# antenna ball
dot(27, "white")
penup()

# eyes
setpos(-32, 80)
dot(27, "#FF4500")
setpos(32, 80)
dot(27, "#FF4500")

# smile
pen(pencolor="#FF4500")
setpos(-32, 50)
seth(320)
pensize(7)
pendown()
circle(50, 80)

done()
