from pico2d import *
import game_world
import game_framework

PIXEL_PER_METER = (1.0 / 0.03)  # 1pixel = 3cm, 1m = 33.33 pixel
GRAVITY = 9.8  # 중력 가속도 (m/s²)

class Ball:
    image = None

    def __init__(self, x = 400, y = 300, throwin_speed = 15, throwin_angle = 45):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y = x, y
        self.xv = throwin_speed * math.cos(math.radians(throwin_angle))  # m/s
        self.yv = abs(throwin_speed * math.sin(math.radians(throwin_angle)))   # m/s
        self.stopped = True if throwin_speed == 0.0 else False
        self.removed=False

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        if self.stopped:
            return
        # 위치 업데이트
        self.x += self.xv * game_framework.frame_time * PIXEL_PER_METER
        self.y += self.yv * game_framework.frame_time * PIXEL_PER_METER

        # y 축 속도에 중력 가속도 적용
        self.yv -= GRAVITY * game_framework.frame_time  # m/s

    def get_bb(self): #공에 대해서 바운딩 박스
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def handle_collision(self, group, other):
        if  self.removed:
            return
        if group == 'boy:ball': #상대편이 boy -사라진다
            self.removed = True
            game_world.remove_object(self) #커리전 페어에서는 없애지않음
        elif group=='grass:ball': #땅에 닿으면 멈춤
            self.stopped = True

        elif group=='ball:zombie':
            self.removed = True
            game_world.remove_object(self)
