from pico2d import *

open_canvas()

grass=load_image('grass.png')


def move_walk():
    print("walk")
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
    move_run()
    move_jump()
    move_attack()

    pass




close_canvas()
