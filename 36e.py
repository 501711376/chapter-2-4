sides=int(input("Whats the number of sides?"))
import turtle
wn = turtle.Screen()
alex=turtle.Turtle()
for i in range(sides):
    alex.forward(40)
    alex.left(360/sides)