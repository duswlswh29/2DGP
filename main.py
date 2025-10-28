from pico2d import *

import game_world
from boy import Boy
from grass import Grass
from front_grass import Front_Grass


# Game object class here


def handle_events():
    global running

    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            boy.handle_event(event)


def reset_world():

    global boy



    grass = Grass() #보이랑 그래스를 담는 순서
    game_world.add_object(grass,2)

    front_grass=Front_Grass()
    game_world.add_object(front_grass,0)


    boy = Boy()
    game_world.add_object(boy,1)




def update_world():
    game_world.update()
    pass


def render_world():
    clear_canvas()
    game_world.render()
    update_canvas()


running = True



open_canvas()
reset_world()
# game loop
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.01)
# finalization code
close_canvas()
