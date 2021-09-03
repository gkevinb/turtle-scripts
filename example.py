from turtle import *

color('yellow', 'blue')

begin_fill()
while True:
    forward(100)
    left(121)
    if abs(pos()) < 1:
        break
end_fill()
done()


# def talloval(r):               # Verticle Oval
#     left(45)
#     for loop in range(2):      # Draws 2 halves of ellipse
#         circle(r,90)    # Long curved part
#         circle(r/2,90)  # Short curved part

# def flatoval(r):               # Horizontal Oval
#     right(45)
#     for loop in range(2):
#         circle(r,90)
#         circle(r/2,90)

# bgcolor("black")
# pen(pencolor="cyan")
# # shape("circle")
# speed(100)
# # circle(100, 190)
# # shapesize(15, 5, 10)
# # stamp()
# # flatoval(200)
# # talloval(200)
# rad = 200
# for i in range(2):
#     # two arcs
#     circle(rad // 4, 60)
#     circle(rad // 2, 60)
