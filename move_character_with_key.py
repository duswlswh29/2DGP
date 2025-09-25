from pico2d import *


open_canvas()
grass = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')


def handle_events():
    global running, dir_x ,dir_y,last_dir
    global x,y

    

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x+=1
                last_dir="right"
            if event.key == SDLK_LEFT:
                dir_x-=1
                last_dir="left"
            if event.key==SDLK_UP:
                dir_y+=1
            if event.key==SDLK_DOWN:
                dir_y-=1
            if event.key == SDLK_ESCAPE:
                running = False
        elif event.type== SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x-=1
            if event.key == SDLK_LEFT:
                dir_x+=1
            if event.key==SDLK_UP:
                dir_y-=1
            if event.key==SDLK_DOWN:
                dir_y+=1



running = True
x = 800 // 2
y=90
frame = 0
dir_x=0
dir_y=0
last_dir="right"



while running:
    clear_canvas()


    grass.draw(400, 100)

    if dir_x!=0 or dir_y!=0:
        if last_dir=="right":
         character.clip_draw(frame * 100, 100, 100, 100, x, y)
        else:
         character.clip_draw(frame * 100, 0, 100, 100, x,y)
    else:
        if last_dir=="right":
         character.clip_draw(frame * 100, 300, 100, 100, x, y)
        else:
         character.clip_draw(frame * 100, 200, 100, 100, x, y)
        delay(0.08)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    x+=dir_x*5
    y+=dir_y*5

    if x>777:
        x=777
    elif x<22:
        x=22
    if y>561:
        y=561
    elif y<37:
          y=37

    delay(0.05)

#완성
close_canvas()

