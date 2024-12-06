print('Trần Văn Tú MSV 235752021610056')
import turtle

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Create the turtle
painter = turtle.Turtle()
painter.pensize(3)

# Define a list of colors to alternate
colors = ['red', 'green', 'blue']

# Draw overlapping circles
for i in range(36):  # 36 circles to complete the pattern
    painter.pencolor(colors[i % 3])  # Alternate between red, green, and blue
    painter.circle(100)  # Draw a circle with a radius of 100
    painter.left(10)  # Rotate by 10 degrees

# Hide the turtle and keep the window open
painter.hideturtle()
window.mainloop()
