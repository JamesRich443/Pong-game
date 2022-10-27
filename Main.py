

from turtle import Screen,Turtle
from board import Board
from ball import Ball
import time
board=Turtle()
screen= Screen()
screen.bgcolor('black')
screen.setup(width=800,height=600)
screen.title("pong")
screen.tracer(0)



r_board=Board((350,0),'white')
l_board=Board((-350,0), 'red')
ball= Ball()
screen.listen()
screen.onkey(r_board.up,"Up")
screen.onkey(r_board.down,"Down")
screen.onkey(l_board.up,"w")
screen.onkey(l_board.down,"s")
on=True
while on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    
    if  ball.distance(r_board)<50 and ball.xcor()>340 or ball.distance(l_board)<50 and ball.xcor() <340:
        ball.bounce_x()



screen.exitonclick()

