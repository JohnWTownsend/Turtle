import turtle
import random

turtle.pensize(1)
turtle.speed(500)
turtle.bgcolor("black")
turtle.hideturtle()

colorList = ["purple", "red", "green", "blue", "orange", "yellow"]

i = 0
while True:
    turtle.color(colorList[int(random.random()*1000)%6])
    
    turtle.forward(1 + i)
    turtle.left(i)  #202.5, 225, 168.75, 174.375
    i += .2

turtle.exitonclick()