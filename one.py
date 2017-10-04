import turtle



def make_sqaure(turt,size,num):
    
    for j in range(num):
        turt.pendown()
     for i in range(4):
         turt.forward(size)
         turt.left(90)
         turt.penup()
         turt.forward(2*size)
        
wn = turtle.Screen()
owen=turtle.turtle()
    
make_sqaure(owen,20,5)