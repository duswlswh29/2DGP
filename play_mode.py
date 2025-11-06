import random
from pico2d import *

import game_framework
import game_world

from boy import Boy
from grass import Grass
from ball import Ball
from zombie import Zombie

boy = None

def handle_events():
    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)

def init():
    global boy

    grass = Grass()
    game_world.add_object(grass, 0)
    game_world.add_collision_pair('grass:ball', grass, None)

    boy = Boy()
    game_world.add_object(boy, 1)

    global balls #바닥에 공 배치
    balls=[Ball(random.randint(100,1600-100),60,0)for _ in range(20)]
    game_world.add_objects(balls,1)

    zombies=[Zombie() for i in range(20)]
    game_world.add_objects(zombies,1)

    #충돌 검사가 필요한 페어를 등록
    game_world.add_collision_pair('boy:ball',boy,None) #아까 만든다고 한 리스트에 boy를 넣음
    for ball in balls:
        game_world.add_collision_pair('boy:ball',None,ball)
        #b리스트에(위에는 a리스트에집어넣는 )ball1 ball2 ball3이 다 들어감
        #충돌 대상이 리스트화해서 들어감
        #이제 일일이 체크하는 일

    for ball in balls:
     game_world.add_collision_pair('ball:zombie',ball,None)

    for zombie in zombies:
        game_world.add_collision_pair('ball:zombie',None,zombie)
def update():
    game_world.update()
    #게임 내 모든 객체가 업데이트가 끝낫기 떄문에 그에 따른 충돌 검사 필요
    game_world.handle_collisions()


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()


def finish():
    game_world.clear()

def pause(): pass
def resume(): pass

