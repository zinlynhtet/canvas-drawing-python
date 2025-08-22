from turtle import *

def setup_canvas():
    reset()
    screensize(600, 600)
    speed(0)
    hideturtle()
def draw_polygon(n):
    for _ in range(n):
        forward(100)
        left(360 / n)

setup_canvas()

n = int(input("Enter a positive integer n (3 ≤ n ≤ 20): "))

if 3 <= n <= 20:
    draw_polygon(n)
else:
    print("Invalid input. Please enter an integer between 3 and 20.")
done