from pico2d import load_image, get_time, load_font
from sdl2 import SDL_KEYDOWN, SDLK_SPACE, SDLK_RIGHT, SDL_KEYUP, SDLK_LEFT

import game_world
import game_framework
from ball import Ball, PIXEL_PER_METER
from state_machine import StateMachine



BIRD_SIZE_M=3.0 #3mx3m 100px x 100px
BIRD_WIDTH=BIRD_SIZE_M * PIXEL_PER_METER
BIRD_HEIGHT=BIRD_SIZE_M * PIXEL_PER_METER

BIRD_SPEED_KMPH=25.0 #km/h
BIRD_SPEED_MPM=(BIRD_SPEED_KMPH * 1000.0 / 60.0)
BIRD_SPEED_MPS=(BIRD_SPEED_MPM / 60.0)
BIRD_SPEED_PPS=(BIRD_SPEED_MPS * PIXEL_PER_METER)

TIMER_PER_ACTION=1.0/3.0
FRAMES_PER_ACTION=14
ACTION_PER_TIME=1.0/TIMER_PER_ACTION #초당 3회 날갯짓 42fps

class Bird:
    image=None

    def __init__(self,x,y,dir=1):
        if Bird.image is None:
            Bird.image=load_image('bird_animation.png')
        self.x,self.y=x,y
        self.dir=dir
        self.frame=0

        pass

    def update(self):
        self.frame=(self.frame+FRAMES_PER_ACTION*ACTION_PER_TIME*game_framework.frame_time)%14
        self.x+=self.dir * BIRD_SPEED_PPS * game_framework.frame_time


        if self.x<20:
           self.dir=1
        elif self.x>1580:
           self.dir=-1

        pass
    def draw(self):
        frame_x = int(self.frame) % 5
        frame_y = int(self.frame) // 5
        left = frame_x * 182
        bottom = (2 - frame_y) * 168

        if self.dir==1:
            self.image.clip_draw(left,bottom,182,168,self.x,self.y,BIRD_WIDTH,BIRD_HEIGHT)
        else:
            self.image.clip_composite_draw(left,bottom,182,168,0,'h',self.x,self.y,BIRD_WIDTH,BIRD_HEIGHT)
        pass

