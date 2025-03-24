
"""
Turtles with a loop. 

Study the previous program, 05a_Loop_with_Turtle.py, and then
write a new program that uses a loop to draw a pentagon.
( You can cut and past most of it! )

"""

... # Your code here
import turtle

# Create turtle object
t = turtle.Turtle()

# Move turtle without drawing
t.penup()
t.goto(0, 0)  # Moved to a more visible location
t.pendown()
t.degrees()

# Draw a shape
for i in range(25):
    t.forward(50)  # Increased distance for visibility
    t.left(72)

# Wait for user click to close the window
turtle.exitonclick()
