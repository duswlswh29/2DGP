world = [[] for _ in range(4)]

def add_object(o, depth = 0):
    world[depth].append(o)


def add_objects(ol, depth = 0):
    world[depth] += ol


def update():
    for layer in world:
        for o in layer:
            o.update()


def render():
    for layer in world:
        for o in layer:
            o.draw()


def remove_collision_object(o):
    for pairs in collision_pairs.values():
        if o in pairs[0]:
            pairs[0].remove(o)
        if o in pairs[1]:
            pairs[1].remove(o)
    pass


def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            #컬리전 페어에서도 제거해주어야함
            remove_collision_object(o)
            return

    raise ValueError('Cannot delete non existing object')


def clear():
    global world

    for layer in world:
        layer.clear()


def collide(a, b):
    left_a,bottom_a,right_a,top_a = a.get_bb()
    left_b,bottom_b,right_b,top_b = b.get_bb()

    # 두 개의 사각형이 충돌하지 않는 경우를 찿아서 false로
    if left_a>right_b: return False
    if right_a<left_b: return False
    if top_a<bottom_b:return False
    if bottom_a>top_b:return False

    return True #충돌이 있다

collision_pairs={} #key 충돌 종료, value: [a],[b]

def add_collision_pair(group,a, b): #그룹을 통해서 가져온담에 a,b리스트를 만듬
    if group not in collision_pairs:
        print('새로운 그룹 추가')
        collision_pairs[group] = [[],[]]

    if a:
     collision_pairs[group][0].append(a) #리스트 안에 {'boy:ball' : [],[]} 이런 구조에서
    if b:
     collision_pairs[group][1].append(b)# [a] [b]를 집어넣음


def handle_collisions():#컬리전 페어에 들어잇는 충돌 조합에 대해서 실제로 충돌을 해줘야 한다
    for group, pairs in collision_pairs.items():
        for a in pairs[0]:
            for b in pairs[1]:
                if collide(a,b): #얘는 얘네들이 소년인지 볼인지 그래스인지 모름 -> 각자 객체에게 충돌 처리를 맡김
                    a.handle_collision(group,b)
                    b.handle_collision(group,a)

    return None