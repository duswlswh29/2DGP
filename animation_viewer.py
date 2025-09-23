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
        sonic.clip_draw(x,y,frame_width,frame_height,400,200,frame_width*10,frame_height*10)

        update_canvas()

        delay(0.1)

    pass

def move_run():
    print("run")
    run_row=6
    run_frames=8

    frame_height=48

    run_x = [0,25, 53, 81, 110, 138, 165, 191]
    run_frame_widths = [25, 28, 28, 29,28 , 27, 26, 25]
    frame=0
    sprite_sheet_height = sonic.h  # 이미지 전체 높이
    y=sonic.h-(run_row+1)*frame_height
    for frame in range(run_frames):
        x=3+run_x[frame]+1
        frame_width=run_frame_widths[frame]

        clear_canvas()
        grass.draw_now(400,30)

        sonic.clip_draw(x,y,frame_width,frame_height,400,200,frame_width*10,frame_height*10)

        update_canvas()

        delay(0.1)

    pass

def repeat_animation(animation_func, repeat_count=5, pause_time=1.0):
    for _ in range(repeat_count):
        animation_func()
    delay(pause_time)


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
            sonic.clip_draw(x,y,frame_width,frame_height,400,200,frame_width*10,frame_height*10)
            update_canvas()
            delay(0.1)


        for col in range(0,2):
          row=3
          x=6+col*frame_width
          y=sonic.h-(row+1)*frame_height
          clear_canvas()
          grass.draw_now(400,30)
          sonic.clip_draw(x,y,frame_width,frame_height,400,200,frame_width*10,frame_height*10)
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
        sonic.clip_draw(x, y, frame_width, frame_height, 400, 220, frame_width * 10, frame_height * 10)

        update_canvas()

        delay(0.1)
    pass




while True:
    grass.draw_now(400,30)
    repeat_animation(move_walk)
    repeat_animation(move_run)
    repeat_animation(move_jump)
    repeat_animation(move_attack)

    pass




close_canvas()
