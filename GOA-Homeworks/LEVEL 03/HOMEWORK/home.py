import turtle

def draw_house():
    """
    Function to draw a house using the turtle module.

    This function uses the turtle module to draw a simple house shape on the screen.

    Returns:
    - None

    Raises:
    - None
    """

    # Create a turtle object
    t = turtle.Turtle()

    # Set the speed of the turtle
    t.speed(1)

    # Draw the base of the house
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)

    # Draw the roof of the house
    t.forward(100)
    t.left(45)
    t.forward(70.71)
    t.left(90)
    t.forward(70.71)
    t.left(45)
    t.forward(100)

    # Draw the door of the house
    t.penup()
    t.goto(50, 0)
    t.pendown()
    t.left(90)
    t.forward(50)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(50)

    # Draw the window of the house
    t.penup()
    t.goto(20, 50)
    t.pendown()
    t.forward(30)
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(30)

    # Hide the turtle
    t.hideturtle()

    # Close the turtle graphics window
    turtle.done()

# Call the function to draw the house
draw_house()