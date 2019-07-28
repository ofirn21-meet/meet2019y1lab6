#import turtle
#num_pts= 4
#for i in range (num_pts):
   # turtle.left(360/num_pts)
    #turtle.forward(100)
#turtle.mainloop()
   
import turtle
turtle.tracer(1)
rounds = 10
size = 10
mike = turtle.clone()
steve = turtle.clone()
turtle.bgcolor("pink")
turtle.hideturtle()
mike.color("gold")
steve.color("purple")
steve.goto(5,5)
while True:
	mike.forward(size)
	mike.left(90)
	steve.forward(-size)
	steve.left(-90)
	size += 10
turtle.mainloop()
