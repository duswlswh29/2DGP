from pico2d import load_image


class Front_Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 70)

    def update(self):
        pass

