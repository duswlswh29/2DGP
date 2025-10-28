#월드에 계층을 준다
# world[0] : 가장 밑에
# world[1]: 그 위에

world=[[],[]]

def add_object(o,depth=0):#뎁스 기본값 설정
    world[depth].append(o)

#월드 전체의 객체를 업데이트
def update():
    for layer in world:
        for o in layer:
         o.update()

#월드 전체의 객체를 그린다
def render():
    for layer in world:
        for o in layer:
         o.draw()

def remove_object(o):
 for layer in world:
     if o in layer:
       layer.remove(o)
       return

 print('월드에 존재하지 않는 객체를 삭제하려고 합니다')