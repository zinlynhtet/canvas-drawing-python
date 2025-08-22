!pip3 install ColabTurtlePlus
from ColabTurtlePlus.Turtle import *

def init_canvas(width=800,height=400):
  # Initialize the canvas
  initializeTurtle(window=(width,height))
  speed(13)

  # Draw the border
  penup()
  goto(-width//2,height//2)
  pendown()
  pencolor("LightGray")
  setheading(0)
  forward(width)
  right(90)
  forward(height)
  right(90)
  forward(width)
  right(90)
  forward(height)

  # Draw X and Y axes
  penup()
  goto(-width//2,0)
  pendown()
  goto(width//2,0)
  penup()
  goto(0,height//2)
  pendown()
  goto(0,-height//2)

  # Go home
  penup()
  home()
  pendown()
  pencolor("Black")
