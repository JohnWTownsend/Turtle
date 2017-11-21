import turtle

turtle.pensize(1)
turtle.speed(100)

i = 0
while True:
    turtle.forward(2)
    turtle.left(i**2)  #202.5, 225, 168.75, 174.375
    i += .1

turtle.exitonclick()