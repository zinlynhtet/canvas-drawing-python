import turtle
import os
class Messages:
    WELCOME = "Welcome to the Line Drawing Visualizer!"
    ERROR_FILE_NOT_FOUND = "Error: File not found."
    ERROR_INVALID_FORMAT = "Error: Invalid line format."
    DRAWING_COMPLETE = "Drawing complete! Close the window to exit."
def draw_canvas(filename):
    
    screen = turtle.Screen()
    screen.title(Messages.WELCOME)
    screen.setup(width=800, height=800)

    pen = turtle.Turtle()
    pen.pensize(2)

    try:
        read_data(filename, pen, screen)
    except FileNotFoundError:
        print(Messages.ERROR_FILE_NOT_FOUND)
    except Exception as e:
        print(f"Error: {e}")


def read_data(filename, pen, screen):
    with open(filename, 'r') as file:
        lines = file.readlines()

    first_point = True
    pen.penup()

    for line in lines:
        line = line.strip()

        if not line:
            pen.penup()
            first_point = True
            continue

        try:
            x, y = map(int, line.split(','))

            pen.goto(x, y)
            if first_point:
                pen.pendown()
                first_point = False
        except ValueError:
            print(f"{Messages.ERROR_INVALID_FORMAT} Line: {line}")
    pen.hideturtle()
    print(Messages.DRAWING_COMPLETE)
    screen.mainloop()
    
base_path = r"C:\your\path\here"
file_name = "picture.txt"
picture_path = os.path.join(base_path, file_name)
draw_canvas(picture_path)
