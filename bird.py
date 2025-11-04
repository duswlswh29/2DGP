from pico2d import load_image, get_time, load_font
from sdl2 import SDL_KEYDOWN, SDLK_SPACE, SDLK_RIGHT, SDL_KEYUP, SDLK_LEFT

import game_world
import game_framework
from ball import Ball, PIXEL_PER_METER
from state_machine import StateMachine



BIRD_SIZE_M=3.0
BIRD_WIDTH=BIRD_SIZE_M * PIXEL_PER_METER
BIRD_HEIGHT=BIRD_SIZE_M * PIXEL_PER_METER

BIRD_SPEED_KMPH=25.0
BIRD_SPEED_MPM=(BIRD_SPEED_KMPH * 1000.0 / 60.0)
BIRD_SPEED_MPS=(BIRD_SPEED_MPM / 60.0)
BIRD_SPEED_PPS=(BIRD_SPEED_MPS * PIXEL_PER_METER)

class Bird:
    image=None

    def __init__(self):
        pass

    def update(self):
        pass
    def draw(self):
        pass

