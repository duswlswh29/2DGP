from pico2d import *
import math
import turtle

open_canvas()

grass=load_image('grass.png')
character=load_image('character.png')

while True:

 x=0
 y=0
 while(x<800):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,90)

    x=x+2

    delay(0.001)

 while(y<500):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(777, y+90)

    y=y+2
    delay(0.001)
 while(x>0):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,565)

    x=x-2
    delay(0.001)

 while(y>0):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(10, y+90)

    y=y-2
    delay(0.001)
 while(x<400):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x, y+90)

    x=x+2
    delay(0.001)
#원 중심은 400 300? 정도로 하고
#반지름은 200
#r코사인세타이용
 x1=400
 y1=300
 r=200

 for deg in range(360,0,-1):
    angle=math.radians(deg)
    xx1=x1+r*math.cos(angle)
    yy1=y1+r*math.sin(angle)
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(xx1, yy1)


    delay(0.001)




close_canvas()