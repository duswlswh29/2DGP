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
    run_row=6
    run_frames=8
    frame_width=30
    frame_height=48

    sprite_sheet_height = sonic.h  # 이미지 전체 높이
    for frame in range(run_frames):
        x=5+frame*frame_width
        y=sonic.h-(run_row+1)*frame_height
        clear_canvas()
        grass.draw_now(400,30)

        sonic.clip_draw(x,y,frame_width,frame_height,400,100,frame_width*3,frame_height*3)

        update_canvas()

        delay(0.1)

    pass


def move_jump():
    print("jump")

    def move_custom_range():
        frame_width=25
        frame_height=48

        for col in range(0,6):
            row=2
            x=col*frame_width+9
            y=sonic.h-(row+1)*frame_height
            clear_canvas()
            grass.draw_now(400,30)
            sonic.clip_draw(x,y,frame_width,frame_height,400,100,frame_width*3,frame_height*3)
            update_canvas()
            delay(0.1)


        for col in range(0,2):
          row=3
          x=6+col*frame_width
          y=sonic.h-(row+1)*frame_height
          clear_canvas()
          grass.draw_now(400,30)
          sonic.clip_draw(x,y,frame_width,frame_height,400,100,frame_width*3,frame_height*3)
          update_canvas()
          delay(0.1)



    move_custom_range()

    pass


def move_attack():
    print("attack")
    attack_row=1
    attack_frames =6
    frame_width = 27
    frame_height = 48

    sprite_sheet_height = sonic.h  # 이미지 전체 높이
    for frame in range(attack_frames):
        x = frame * frame_width + 5
        y = sonic.h - (attack_row + 1) * frame_height
        clear_canvas()
        grass.draw_now(400, 30)
        sonic.clip_draw(x, y, frame_width, frame_height, 400, 100, frame_width * 3, frame_height * 3)

        update_canvas()

        delay(0.1)
    pass


while True:
    grass.draw_now(400,30)
    #move_walk()
    #move_run()
    #move_jump()
    move_attack()

    pass




close_canvas()
