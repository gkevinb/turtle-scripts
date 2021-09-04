from turtle import *
bgcolor("black")
speed(1)
seth(90)
forward(100)
dot(220, "#1DB954")
pen(pencolor="black")
hideturtle()
for i in range(3):
    penup()
    goto(10*i+50, 31.5*i+56)
    pendown()
    width(i*3+14)
    seth(150)
    circle(20*i+120, 50)
done()



# pen(pencolor="gray")

# penup()
# goto(50, 56)
# pendown()
# width(14)
# seth(150)
# circle(120, 50)

# penup()
# goto(60, 86) # +10, 30
# pendown()
# width(17) # +3
# seth(150)
# circle(140, 50) # +20

# penup()
# goto(70, 119) # +10, 32
# pendown()
# width(20) # +3
# seth(150)
# circle(160, 50) # +20