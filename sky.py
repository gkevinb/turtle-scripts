from turtle import *
import random

speed(1000)
hideturtle()
bgcolor("black")
for i in range(1000):
    x = random.randint(-300, 300)
    y = random.randint(-400, 400)
    goto(x, y)
    dot(2, "white")
done()