from pico2d import open_canvas, delay, close_canvas
import game_framework

import play_mode as start_mode

open_canvas(1600, 600)
game_framework.run(start_mode)
close_canvas()

# 새 크기가 얼마냐 3MX3M 단위를 쓰고 새의 속도는 지피티한테 물어볼 수 있다
