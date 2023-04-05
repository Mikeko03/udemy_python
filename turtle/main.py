from turtle import Turtle, Screen

timmy = Turtle()

print(timmy)

my_screen = Screen()
timmy.shape("turtle")
timmy.color("blue")

while True:
    timmy.forward(100)
    timmy.left(75)

my_screen.exitonclick()