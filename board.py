from turtle import Screen,Turtle

class Board(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(position)

        
    def up(self):
        y_up=self.ycor()+20
        self.goto(self.xcor(),y_up)

    def down(self):
         y_up=self.ycor()-20
         self.goto(self.xcor(),y_up)   
        