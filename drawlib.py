import turtle
import time
import random

turtle.Screen().bgcolor("black")
turtle.color("green")

def cube(size):
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(45)
    turtle.forward(size / 2)
    turtle.right(45)
    turtle.forward(size)
    turtle.right(135)
    turtle.forward(size / 2)
    turtle.backward(size / 2)
    turtle.left(45)
    turtle.forward(size)
    turtle.right(45)
    turtle.forward(size / 2)
    turtle.backward(size / 2)
    turtle.right(45)
    
    turtle.exitonclick()
    
    
#cube()
def glascube(size):
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(45)
    turtle.forward(size / 2)
    turtle.right(45)
    turtle.forward(size)
    turtle.right(135)
    turtle.forward(size / 2)
    turtle.backward(size / 2)
    turtle.left(45)
    turtle.forward(size)
    turtle.right(45)
    turtle.forward(size / 2)
    turtle.backward(size / 2)
    turtle.right(45)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.backward(size)
    turtle.left(135)
    turtle.forward(size / 2)
    
    turtle.exitonclick()
    
glascube(int(input("Size: ")))