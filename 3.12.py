import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
aq = turtle.Turtle()
aq.shape("turtle")
aq.color("blue")
aq.stamp()
angle=0
for i in range(12):
    angle=angle+30
    aq.right(angle)
    aq.penup()
    aq.forward(200)
    aq.pendown()
    aq.forward(20)
    aq.penup()
    aq.forward(12)
    aq.stamp()
    aq.home()

wn.mainloop()