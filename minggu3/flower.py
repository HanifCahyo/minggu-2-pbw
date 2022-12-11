from turtle import *

bgcolor ('black')
tracer (3)

col=['blue','pink','yellow','red','green','violet']
for i in range(120):
    pencolor(col[i%6])
    circle(190-i/2,90)
    lt (90)
    circle(190-i/3,90)
    lt (60)