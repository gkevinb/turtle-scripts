from turtle import *
def diamond(x, y):
    seth(0)
    goto(x, y)
    stamp()
    seth(180)
    forward(53)
    stamp()
speed(100)
bgcolor("white")
pen(pencolor="#0060FF")
shape("triangle")
fillcolor("#0060FF")
penup()
width(1)
shapesize(5, 4.5, 1)
diamond(20, 6)
diamond(108, 70)
diamond(-68, 70)
diamond(108, 172)
diamond(-68, 172)
done()

# from turtle import *

# def diamond(x, y):
#     seth(0)
#     goto(x, y)
#     stamp()
#     seth(180)
#     forward(47)
#     stamp()

# speed(100)
# bgcolor("#0060FF")
# pen(pencolor="white")
# shape("triangle")
# fillcolor("white")
# penup()
# width(1)
# shapesize(5, 4, 1)


# diamond(20, 6)
# diamond(90, 70)
# diamond(-50, 70)
# diamond(90, 172)
# diamond(-50, 172)



done()