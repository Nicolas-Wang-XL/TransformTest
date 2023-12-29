import math


def a_muti_b(a, b):
    r = [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]
    for x in range(len(a)):
        for y in range(len(a[x])):
            for t in range(len(a[x])):
                r[x][y] += a[x][t]*b[t][y]
    return r


def p_muti_t(p, t):
    r = [0, 0, 0, 0]
    for x in range(len(p)):
        for y in range(len(p)):
            r[x] += t[x][y] * p[y]
    return r
    

def left_to_right(trans_left):
    z = [[1, 0, 0, 0],
         [0, 1, 0, 0],
         [0, 0,-1, 0],
         [0, 0, 0, 1]]
    r = a_muti_b(z, trans_left)
    r = a_muti_b(r, z)
    return r


def right_move(p, x, y, z, enable_left=False):
    t = [[1, 0, 0, x],
         [0, 1, 0, y],
         [0, 0, 1, z],
         [0, 0, 0, 1]]
    if enable_left:
        t = left_to_right(t)
    # print(t)
    return p_muti_t(p, t)


def right_trans(p, x, y, z, enable_left=False):
    z_trans = [[math.cos(z),-math.sin(z), 0, 0],
               [math.sin(z), math.cos(z), 0, 0],
               [           0,          0, 1, 0],
               [           0,          0, 0, 1]]
    x_trans = [[1,           0,           0, 0],
               [0, math.cos(x),-math.sin(x), 0],
               [0, math.sin(x), math.cos(x), 0],
               [           0,          0, 0, 1]]
    y_trans = [[ math.cos(y), 0, math.sin(y), 0],
               [           0, 1,           0, 0],
               [-math.sin(y), 0, math.cos(y), 0],
               [           0, 0,           0, 1]]
    t = a_muti_b(x_trans, y_trans)
    t = a_muti_b(t, z_trans)
    # print(t)
    if enable_left:
        t = left_to_right(t)
    # print(t)
    return p_muti_t(p, t)


if __name__ == "__main__":
    p = [1, 1, 1, 1]
    print(right_move(p, 1, 0, 0))
    print(right_move(p, 0, 1, 0))
    print(right_move(p, 0, 0, 1))
    print("left")
    print(right_move(p, 1, 0, 0, True))
    print(right_move(p, 0, 1, 0, True))
    print(right_move(p, 0, 0, 1, True))
    print("right")
    print(right_trans(p, math.pi/2, 0, 0))
    print(right_trans(p, 0, math.pi/2, 0))
    print(right_trans(p, 0, 0, math.pi/2))
    # print()
    # print(p)
    print("left")
    print(right_trans(p, math.pi/2, 0, 0, True))
    # print()
    # print(p)
    print(right_trans(p, 0, math.pi/2, 0, True))
    # print()
    # print(p)
    print(right_trans(p, 0, 0, math.pi/2, True))