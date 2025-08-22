from turtle import *

def setup_canvas():
    reset()
    screensize(600, 600)
    speed(0)
    hideturtle()

def draw_cube():
    setup_canvas()
    penup()
    goto(-100, -100)
    pendown()
    for _ in range(4):
        forward(200)
        left(90)

    penup()
    goto(-50, -50)
    pendown()
    for _ in range(4):
        forward(200)
        left(90)

    # connect corners
    penup(); goto(-100, -100); pendown(); goto(-50, -50)
    penup(); goto(100, -100); pendown(); goto(150, -50)
    penup(); goto(100, 100);  pendown(); goto(150, 150)
    penup(); goto(-100, 100); pendown(); goto(-50, 150)

def draw_nested_squares():
    setup_canvas()
    sizes = [100, 150, 200]
    for s in sizes:
        penup()
        goto(-s/2, -s/2)
        pendown()
        for _ in range(4):
            forward(s)
            left(90)

    penup()
    goto(-250, 0)
    pendown()
    forward(500)

def draw_cubic_curve():
    setup_canvas()

    penup(); goto(-250, 0); pendown(); forward(500)  # x-axis
    penup(); goto(0, -250); pendown(); setheading(90); forward(500)  # y-axis

    penup()
    scale = 20
    goto(-200, ((-200/scale)**3 - (-200/scale)) * scale)
    pendown()
    for x in range(-200, 201, 2):
        y = (x/scale)**3 - (x/scale)
        goto(x, y * scale)

    setheading(45)
    forward(20)
    backward(20)
    right(90)
    forward(20)
    backward(20)

# draw_cube()
# draw_nested_squares()
#draw_cubic_curve()

done()