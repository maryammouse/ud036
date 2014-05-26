import turtle


def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)



def draw_art():
    wn = turtle.Screen()
    wn.bgcolor("hotpink")
    #Tara = turtle.Turtle()
    #Tara.shape("turtle")
    #Tara.color("purple")
    #i = 0
    #while i < 4:
        #Tara.forward(100)
        #Tara.right(90)
        #i += 1
    #Gabby = turtle.Turtle()
    #Gabby.shape("arrow")
    #Gabby.circle(100)
#
    Nyssa = turtle.Turtle()
    Nyssa.speed(0)
    #Nyssa.forward(100)
    #Nyssa.right(135)
    #Nyssa.forward(100)
    #Nyssa.right(135)
    #Nyssa.forward(100)
    #Nyssa.right(45)

    for i in range(1, 75):
        draw_square(Nyssa)
        Nyssa.right(5)


    wn.exitonclick()



draw_art()
