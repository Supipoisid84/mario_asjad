#Alex Kreimann
#08.11.2024
#Mission Impossible

import turtle

turtle.pensize(2)
turtle.pendown
turtle.speed(0)

majade_suurused=[50,75,100,75,50,75]

for majade_suurus in majade_suurused:
    for sein in range(4):
        turtle.forward(majade_suurus)
        turtle.left(90)

    turtle.forward(majade_suurus*0.3)
    turtle.left(90)
    turtle.color("blue")
    turtle.forward(majade_suurus*0.7)
    turtle.right(90)
    turtle.forward(majade_suurus*0.4)
    turtle.right(90)
    turtle.forward(majade_suurus*0.7)
    turtle.color("black")
    turtle.right(90)
    turtle.forward(majade_suurus*0.7)


    turtle.right(90)
    turtle.forward(majade_suurus)
    turtle.right(90)

    turtle.color("green")
    for katus in range(3):
        turtle.forward(majade_suurus)
        turtle.left(120)
    turtle.color("black")

    turtle.forward(majade_suurus)
    turtle.penup()
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(majade_suurus)
    turtle.left(90)
    turtle.pendown()

turtle.done()
