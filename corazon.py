import turtle 
import time
pen = turtle.Turtle() 
  
def curve(): 
    for i in range(200): 
        pen.right(1) 
        pen.forward(1) 
  
def heart(): 
  
    pen.fillcolor('red') 
    pen.begin_fill() 
    pen.left(140) 
    pen.forward(113) 
    curve() 
    pen.left(120)
    curve() 
    pen.forward(112)    
    pen.end_fill() 
  
def txt(): 
  
    pen.up() 
    pen.setpos(-85, 85) 
    pen.down() 
    pen.color("white") 
    pen.write("Te Quiero Paula", font=("Verdana", 15, "bold")) 
  
heart() 
  
txt() 
time.sleep(10)  
pen.ht() 