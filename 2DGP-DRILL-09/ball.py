from pico2d import load_image

import game_world


class Ball:
    image=None

    def __init__(self,x=400,y=300,velocity=1):
        if not Ball.image:
            Ball.image=load_image('ball21x21.png')
        self.x,self.y,self.velocity=x,y,velocity

    def draw(self):
        self.image.draw(self.x,self.y)

    def update(self):
        self.x+=self.velocity

        if self.x<25 or self.x>800-25: #볼이 화면을 넘어가면 game world로부터 자기자신을 삭제하도록
            game_world.remove_object(self)

