# checkers-stuckers
DIM = 8

class Player:
    def __init__(self, human, items, directions):
        self.human = human
        self.items = items
        self.directions = directions      
      
board = 0xaa55aa55aa55aa55

DIR_LT = 7
DIR_RT = 9
DIR_UP = True
DIR_DN = False

p1=Player(True, [0x1, 0x4, 0x10, 0x40], DIR_UP)
p2=Player(False, [0x8000000000000000, 0x2000000000000000,
         0x0800000000000000, 0x0200000000000000], DIR_DN)

def display(val):
    s = format(val, 'b').zfill(64)[::-1]
    out = ''
    for i in range(64, 0, -8):
        out = out + s[i - 8:i] + '\n'
    print(out)

def show_board():
    o = sum(p1.items)
    t = sum(p2.items)
    out = ''
    ret = ''
    for i in range(0, 64):
        s = ' '
        s = '·' if 1 & board >> i else ' '
        if 1 & o >> i:
            s = 'o'
        if 1 & t >> i:
            s = '*'
        out = out + s
    for i in range(64, 0, -8):
        ret = '{0}{1}\n'.format(ret, out[i - 8:i])
    print(ret)

def ask():
    direction = 0
    n=0
    n = input('Введите номер фигуры [{0}-{1}]:'.format(0, len(our)-1))
    if n == 'q':
        quit()
    if n.isdigit():
        print(n)
        d = input("Введите направление движения (l или r):")
        if d == 'l':
            direction = DIR_LT
        if d == 'r':
            direction = DIR_RT
        print(direction)
    return (n, direction)

def calculate(item, direction):
    rr = rl = 0
    cr = item<<DIR_RT if direction == DIR_UP else item>>DIR_RT
    cl = item<<DIR_LT if direction == DIR_UP else item>>DIR_LT
    
    if step_allow(cr):
        rr = 1 + calculate(cr, direction)
    if step_allow(cl):
        rl = 1 + calculate(cl, direction)
    return (rr+rl)

def step_allow(item):
    return True if (item & (board ^ sum(p1.items) ^ sum(p2.items))) > 0 else False

# Вот тут изменить надо
def move_item(p, direction, incr):
    c = our[item]<<incr if direction == DIR_UP else our[item]>>incr 
    if step_allow(c):
        our[item] = c
    else:
        print("Неверный ход...")

if __name__ == "__main__": 
    working = True

    while working:

    #    display(sum(our))
        show_board()
        if p1.human:
            n,d = ask()
            move_item(int(n), DIR_UP, d)



        
