from pico2d import *

open_canvas()

grass=load_image('grass.png')
sonic=load_image('sonic-sprite1.png')


def move_walk():
    print("walk")
    walk_row=4
    walk_frames=8
    frame_width=29
    frame_height=48

    sprite_sheet_height = sonic.h  # 이미지 전체 높이
    for frame in range(walk_frames):


        x=frame*frame_width+5
        y=sonic.h-(walk_row+1)*frame_height
        clear_canvas()
        grass.draw_now(400,30)
        sonic.clip_draw(x,y,frame_width,frame_height,400,100,frame_width*3,frame_height*3)

        update_canvas()

        delay(0.1)

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
