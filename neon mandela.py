import turtle
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Neon Mandala")

#part 2
board = turtle.Turtle()
board.speed("fastest")
board.hideturtle()

#part 3
colors = ["red", "orange", "yellow", "lime", "cyan", "violet", "pink", "white"]
for i in range(80):
    board.color(colors[i % len(colors)])
    board.width(2)
    board.forward(i * 2)
    board.right(91)

#part 4
board.penup()
board.goto(0, -60)
board.setheading(90)
board.pendown()
board.color("gold", "yellow")
board.begin_fill()
for i in range(5):
    board.forward(130)
    board.right(144)
board.end_fill()

#part 5
board.penup()
board.goto(0, 0)
board.pendown()
petal_colors = ["cyan", "lime", "violet", "orange", "deeppink"]
for i in range(36):
    board.color(petal_colors[i % len(petal_colors)])
    board.begin_fill()
    for j in range(4):
        board.forward(55)
        board.right(90)
    board.end_fill()
    board.right(10)
turtle.done()
