#This is Tic Tac Toe by Vanessa Tostado

from graphics import *
from random import *




def grid(win):
   
   rect1 = Rectangle(Point(0,700),Point(200, 500))# Rectangle 1
   rect1.draw(win)
   label=Text(Point(100,600), "1")
   label.draw(win)
   
   rect2 = Rectangle(Point(0,500),Point(200, 300))# Rectangle 2
   rect2.draw(win)
   labe2=Text(Point(100,400), "2")
   labe2.draw(win)

   rect3 = Rectangle(Point(0,300),Point(200, 100))# Rectangle 3
   rect3.draw(win)
   label3=Text(Point(100,200), "3")
   label3.draw(win)


   rect4 = Rectangle(Point(200,700),Point(400, 500))# Rectangle 4
   rect4.draw(win)
   label4=Text(Point(300,600), "4")
   label4.draw(win)

   rect5 = Rectangle(Point(200,500),Point(400, 300))# Rectangle 5
   rect5.draw(win)
   label5=Text(Point(300,400), "5")
   label5.draw(win)


   rect6 = Rectangle(Point(200,300),Point(400, 100))# Rectangle 6
   rect6.draw(win)
   label6=Text(Point(300,200), "6")
   label6.draw(win)


   rect7 = Rectangle(Point(400,700),Point(600, 500))# Rectangle 7
   rect7.draw(win)
   label7=Text(Point(500,600), "7")
   label7.draw(win)

   rect8 = Rectangle(Point(400,500),Point(600, 300))# Rectangle 8
   rect8.draw(win)
   label8=Text(Point(500,400), "8")
   label8.draw(win)
   
   rect9 = Rectangle(Point(400,300),Point(600, 100))# Rectangle 9
   rect9.draw(win)
   label9=Text(Point(500,200), "9")
   label9.draw(win)


def game(win):
   
   Player1="X"
   Player2="Y"
   point = win.getMouse()
   PointX= point.getX()
   PointY=point.getY()
   print PointX
   print PointY
   available=[1,2,3,4,5,6,7,8,9]
   winning=[]
   lose=[]
   possibilities=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
   User = True
  
   while User == True:
      
      point = win.getMouse()
      PointX= point.getX()
      PointY=point.getY()
      print PointX
      print PointY
      
      
      
      if 0<PointX<200 and 500<PointY<700:#Square 1- set parameters for square that has the #1
          X= Text(Point(100,600), "X")#Places a red X on where the user clicked
          X.setTextColor("red")
          X.setSize(36)
          X.draw(win)
          available.remove(1)# appends the number 1 from list of available places computer can choose from
          winning.append(1)
          
      if  0<PointX<200 and 300<PointY<500:#2
          X= Text(Point(100,400), "X")
          X.setTextColor("red")
          X.setSize(36)
          X.draw(win)
          available.remove(2)
          winning.append(2)
         

      if  0<PointX<200 and 100<PointY<300:#3
          X= Text(Point(100,200), "X")
          X.setTextColor("red")
          X.setSize(36)
          X.draw(win)
          available.remove(3)
          winning.append(3)
          
      if  200<PointX<400 and 500<PointY<700:#4
          X= Text(Point(300,600), "X")
          X.setTextColor("red")
          X.setSize(36)
          X.draw(win)
          available.remove(4)
          winning.append(4)
       
          
      if  200<PointX<400 and 300<PointY<500:#5
          X= Text(Point(300,400), "X")
          X.setTextColor("red")
          X.setSize(36)
          X.draw(win)
          available.remove(5)
          winning.append(5)
       
         
      if  200<PointX<400 and 100<PointY<300:#6
          X= Text(Point(300,200), "X")
          X.setTextColor("red")
          X.setSize(36)
          X.draw(win)
          available.remove(6)
          winning.append(6)
         
          
      if  400<PointX<600 and 500<PointY<700:#7
          X= Text(Point(500,600), "X")
          X.setTextColor("red")
          X.setSize(36)
          X.draw(win)
          available.remove(7)
          winning.append(7)
       
         
      if  400<PointX<600 and 300<PointY<500:#8
          X= Text(Point(500,400), "X")
          X.setTextColor("red")
          X.setSize(36)
          X.draw(win)
          available.remove(8)
          winning.append(8)
     
          

      if  400<PointX<600 and 100<PointY<300:#9
          X= Text(Point(500,200), "X")
          X.setTextColor("red")
          X.setSize(36)
          X.draw(win)
          available.remove(9)
          winning.append(9)
          
      print "winning" + str(winning)


    

    
      randNum = choice(available)
      print "Random number " + str( randNum)
      time.sleep(1)
      
      if randNum== 1:
         O=Text(Point(100,600), "O")
         O.setTextColor("blue")
         O.setSize(36)
         O.draw(win)
         available.remove(1)
         lose.append(1)
      

      if randNum==2:
         O= Text(Point(100,400), "O")
         O.setTextColor("blue")
         O.setSize(36)
         O.draw(win)
         available.remove(2)
         lose.append(2)
         
         

      if randNum==3:
          O= Text(Point(100,200), "O")
          O.setTextColor("blue")
          O.setSize(36)
          O.draw(win)
          available.remove(3)
          lose.append(3)
          
          
          
      if randNum==4:
         O= Text(Point(300,600), "O")
         O.setTextColor("blue")
         O.setSize(36)
         O.draw(win)
         available.remove(4)
         lose.append(4)
     
         
         
      if randNum==5:
         O= Text(Point(300,400), "O")
         O.setTextColor("blue")
         O.setSize(36)
         O.draw(win)
         available.remove(5)
         lose.append(5)
       
        
         
      if randNum==6:
         O=Text(Point(300,200), "O")
         O.setTextColor("blue")
         O.setSize(36)
         O.draw(win)
         available.remove(6)
         lose.append(6)
         

         
      if randNum==7:
         O= Text(Point(500,600), "O")
         O.setTextColor("blue")
         O.setSize(36)
         O.draw(win)
         available.remove(7)
         lose.append(7)
       
         
      if randNum==8:
         O= Text(Point(500,400), "O")
         O.setTextColor("blue")
         O.setSize(36)
         O.draw(win)
         available.remove(8)
         lose.append(8)
        
        
         
      if randNum ==9:
         O= Text(Point(500,200), "O")
         O.setTextColor("blue")
         O.setSize(36)
         O.draw(win)
         available.remove(9)
         lose.append(9)


      print "Lose" + str(lose)

      if winning in possibilities:
            print "You Win"
            User== False
      elif lose in possibilities:
            print "You Lose"
            User == False
    
         
def main():
   win = GraphWin('Tic Tac Toe', 700,700) # give title and dimensions
   win.yUp()
   grid(win)
   game(win)
   
   
  

main()

