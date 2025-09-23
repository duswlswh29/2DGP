from pico2d import *

open_canvas()

boy=load_image('character.png')
grass=load_image('grass.png')


def move_top():
    print('Moving top')

    for x in range(790,0,-5):
        draw_boy(x, 550)
    pass


def move_right():
    print('Moving right')
    grass.draw_now(400, 30)
    for y in range(90,550,5):
        draw_boy(780,y)
    pass


def move_bottom():
    print('Moving bottom')
    grass.draw_now(400, 30)
    for x in range(0,790,5):
        draw_boy(x, 90)
    pass


def move_left():
    print('Moving left')
    grass.draw_now(400, 30)
    for y in range(550,90,-5):
        draw_boy(10,y)
    pass


def move_rectangle():
    print("Move rectangle")
    move_bottom()
    move_right()
    move_top()
    move_left()
    clear_canvas_now()
    pass


def move_edge1():
    for t in range(0,101):
        x=x1+(x2-x1)*t/100
        y=y1+(y2-y1)*t/100
        draw_boy(x,y)
    pass


def move_edge2():
    for t in range(0,101):
        x=x2+(x3-x2)*t/100
        y=y2+(y3-y2)*t/100
        draw_boy(x,y)
    pass


def move_edge3():
    for t in range(0,101):
        x=x3+(x1-x3)*t/100
        y=y3+(y1-y3)*t/100
        draw_boy(x,y)
    pass


def move_triangle():
    print("Move triangle")
    global x1,y1,x2,y2,x3,y3
    x1,y1=100,90
    x2,y2=700,90
    x3,y3=400,500 #꼭짓점지정
    move_edge1()
    move_edge2()
    move_edge3() #반시계방향

    pass


def move_circle():
    print("Move circle")
    r=200
    for deg in range(360,0,-1):
        x=r*math.cos(math.radians(deg))+400
        y=r*math.sin(math.radians(deg))+300
        draw_boy(x, y)

    pass


def draw_boy(x: float, y: float):
    clear_canvas_now()
    grass.draw_now(400,30)
    boy.draw_now(x, y)
    delay(0.01)


while True:
    grass.draw_now(400,30)
    move_rectangle()
    move_triangle()
    move_circle()

    pass




close_canvas()
