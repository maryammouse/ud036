import turtle

def flower():
    window = turtle.Screen()
    Flora = turtle.Turtle()
    Flora.speed(0)

    for i in range(1,75):
        Flora.forward(100)
        Flora.right(15)
        Flora.forward(100)
        Flora.right(135)
        Flora.forward(150)
        Flora.right(5)
    Flora.forward(100)
    Flora.right(140)
    Flora.forward(500)

    window.exitonclick()

flower()
