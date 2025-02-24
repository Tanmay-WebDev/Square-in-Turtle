import turtle

turtle.Screen().bgcolor("#6bb2ed")

screenSize = turtle.Screen()
screenSize.setup(500 , 500)

turtle.title("Welcome To Turtle")

board = turtle.Turtle()

for i in range(4):
    board.forward(200)
    board.left(90)
    i = i+1