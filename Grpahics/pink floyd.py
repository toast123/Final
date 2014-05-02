
from graphics import *
 
def main():
   win = GraphWin('Pink Floyd', 700, 700) # give title and dimensions
   win.yUp()
   win.setBackground('black')

   # Main Circle
   cir1 = Circle(Point(350,350), 250)
   cir1.setFill('white')
   cir1.draw(win)
   #inner circle
   cir2 = Circle(Point(350,350), 140)
   cir2.setFill('blue')
   cir2.draw(win)
   #pupil
   cir3 = Circle(Point(350,350), 45)
   cir3.setFill('black')
   cir3.draw(win)
   #center
   cir4 = Circle(Point(350,350), 12)
   cir4.setFill('white')
   cir4.draw(win)

   #movement

   for i in range(10):
        cir3.move(5, 0)
        cir4.move(6,0)
        time.sleep(.05)

   for i in range(19):
        cir3.move(-5, 0)
        cir4.move(-6,0)
        time.sleep(.05)
   

   """
   # Main Triangle

   tri1= Polygon(Point(350,510) , Point(150,230),Point(550,230))
   tri1.setFill("black")
   tri1.setWidth(5)
   tri1.draw(win)

   #rectangle 1
   line1=Line(Point(145, 105), Point(155, 105))
   line1.setFill("yellow")
"""
   

   

main()
