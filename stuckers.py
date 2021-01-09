# checkers-stuckers
DIM = 8
board = 0xaa55aa55aa55aa55

DIR_LT = 7
DIR_RT = 9
DIR_UP = True
DIR_DN = False

class Player:

    preferred_item: int = 0
    preferred_incr: int = DIR_RT

    def __init__(self, name, human, items, direction):
        self.name = name
        self.human = human
        self.items = items
        self.direction = direction
        self.homerow = 0x55 if self.direction == DIR_UP else 0xAA00000000000000

    def move_item(self):
        c = self.items[self.preferred_item]<<self.preferred_incr if self.direction == DIR_UP \
        else self.items[self.preferred_item]>>self.preferred_incr 
        if step_allow(c):
            self.items[self.preferred_item] = c
            return True
        else:
            print("{}: Неверный ход...".format(self.name))
            return False
      
    def ask(self):
        n=0
        n = input('Введите номер фигуры [{0}-{1}]:'.format(0, len(self.items)-1))
        if n == 'q':
            return False
        if n.isdigit():
            self.preferred_item = int(n)
            d = input("Введите направление движения (l или r):")
            if d == 'l':
                self.preferred_incr = DIR_LT
            if d == 'r':
                self.preferred_incr = DIR_RT
        return True

p1=Player('1', True, [0x1, 0x4, 0x10, 0x40], DIR_UP)
p2=Player('2', False, [0x8000000000000000, 0x2000000000000000,
         0x0800000000000000, 0x0200000000000000], DIR_DN)

def display(val):
    s = format(val, 'b').zfill(64)[::-1]
    out = ''
    for i in range(64, 0, -8):
        out = out + s[i - 8:i] + '\n'
    print(out)

def show_board(sum_items1, sum_items2):
    o = sum_items1
    t = sum_items2
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

if __name__ == "__main__": 
    working = True

    while working:

        show_board(sum(p1.items), sum(p2.items))
        if p1.human:
            p1.ask()
            p1.move_item()



        
