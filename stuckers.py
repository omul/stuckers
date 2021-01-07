# checkers-stuckers
DIM = 8

board = 0xaa55aa55aa55aa55
our = [0x1, 0x4, 0x10, 0x40]
their = [0x8000000000000000, 0x2000000000000000,
         0x0800000000000000, 0x0200000000000000]


def display(val):
    s = format(val, 'b').zfill(64)[::-1]
    out = ''
    for i in range(64, 0, -8):
        out = out + s[i - 8:i] + '\n'
    print(out)


def show_board():
    o = sum(our)
    t = sum(their)
    out = ''
    ret = ''
    for i in range(0, 64):
        s = ' '
        s = '.' if 1 & board >> i else ' '
        if 1 & o >> i:
            s = 'o'
        if 1 & t >> i:
            s = '*'
        out = out + s
    #        if i%8 == 0:
    #            out = '\n' + out
    for i in range(64, 0, -8):
        ret = '{0}{1}\n'.format(ret, out[i - 8:i])
    print(ret)


def step_test(item, step):
    if (item << step & (board ^ sum(our) ^ sum(their))) > 0:
        return 1
    else:
        return -1


# def count_movies(table=_table):

def step_our(item, direction):
    incr = 9 if direction else 7
    if step_test(our[item], incr) > 0:
        our[item] = our[item] << incr
    else:
        print("Неверный ход...")


def step_their():
    none


working = True
while working:

    #    display(sum(our))
    show_board()
    nitem = input("Введите номер фигуры или q для выхода:")
    if nitem == 'q':
        break
    if nitem.isdigit():
        print(nitem)
        direction = input("Введите направление движения (l или r):")
        if direction == 'l' or direction == 'r':
            print(direction)
            step_our(int(nitem), True if direction == 'r' else False)
