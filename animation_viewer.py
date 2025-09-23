from pico2d import *

open_canvas()

grass=load_image('grass.png')
sonic=load_image('sonic-sprite1.jpg')


def move_walk():
    print("walk")
    frame=0
    for x in range(0,800,10):
        clear_canvas()
        grass.draw(400,30)
        sonic.clip_draw(frame*44,0,44,44,x,90)
        update_canvas()
        frame=(frame+1)%8
        delay(0.05)
    pass


def move_run():
    print("run")
    pass


def move_jump():
    print("jump")
    pass


def move_attack():
    print("attack")
    pass


while True:
    grass.draw_now(400,30)
    move_walk()
    #move_run()
    #move_jump()
    #move_attack()

    pass




close_canvas()
