# checkers-stuckers
DIM = 8

DIR_LT = 7
DIR_RT = 9
DIR_UP = True
DIR_DN = False


class Table:
    board = 0xaa55aa55aa55aa55
    items = {}
    
    def show_board():
        l = list(Table.items.values())
        o = l[0]
        t = l[1]
        out = ''
        ret = ''
        for i in range(0, 64):
            s = ' '
            s = '·' if 1 & Table.board >> i else ' '
            if 1 & o >> i:
                s = 'o'
            if 1 & t >> i:
                s = '*'
            out = out + s
        for i in range(64, 0, -8):
            ret = '{0}{1}\n'.format(ret, out[i - 8:i])
        print(ret)

    def allow(item):
        b = sum(list(Table.items.values()))
        return True if (item & (Table.board ^ b)) > 0 else False


class Player:

    preferred_item: int = 0
    preferred_incr: int = DIR_RT

    def __init__(self, name, human, items, direction):
        self.name = name
        self.human = human
        self.items = items
        self.direction = direction
        self.homerow = 0x55 if self.direction == DIR_UP else 0xAA00000000000000
        self.edgerow = 0xAA00000000000000 if self.direction == DIR_UP else 0x55
        Table.items[self.name] = sum(self.items)

    def ask(self):
        n=0 
        n = input('{0}: Введите номер фигуры [{1}-{2}]:'.format(self.name, 0, len(self.items)-1))
        if n == 'q':
            return False
        if n.isdigit():
            self.preferred_item = int(n)
            d = input("{0}: Введите направление движения (l или r):".format(self.name))
            if d == 'l':
                self.preferred_incr = DIR_LT
            if d == 'r':
                self.preferred_incr = DIR_RT
        return True

    def move_item(self):
        c = self.items[self.preferred_item]<<self.preferred_incr if self.direction == DIR_UP \
        else self.items[self.preferred_item]>>self.preferred_incr 
        if Table.allow(c):
            if c & self.edgerow:
                self.items.pop(self.preferred_item)
                self.bifurcation()
            else:
                self.items[self.preferred_item] = c
            Table.items[self.name] = sum(self.items)
            return True
        else:
            print("{}: Неверный ход...".format(self.name))
            return False

    def bifurcation(self):
        pass

    def moving_items(self):
        n = 0
        if not self.items:
            return 0
        for i in self.items:
            if Table.allow(i<<DIR_RT if self.direction == DIR_UP else i>>DIR_RT) or \
                Table.allow(i<<DIR_LT if self.direction == DIR_UP else i>>DIR_LT):
                n+=1
        return n
      
def display(val):
    s = format(val, 'b').zfill(64)[::-1]
    out = ''
    for i in range(64, 0, -8):
        out = out + s[i - 8:i] + '\n'
    print(out)

def calculate(item, direction):
    rr = rl = 0
    cr = item<<DIR_RT if direction == DIR_UP else item>>DIR_RT
    cl = item<<DIR_LT if direction == DIR_UP else item>>DIR_LT
    
    if step_allow(cr):
        rr = 1 + calculate(cr, direction)
    if step_allow(cl):
        rl = 1 + calculate(cl, direction)
    return (rr+rl)


if __name__ == "__main__":
    
    p1=Player('1', True, [0x1, 0x4, 0x10, 0x40], DIR_UP)
#   p2=Player('2', False, [0x8000000000000000, 0x2000000000000000, 
#             0x0800000000000000, 0x0200000000000000], DIR_DN)
    p2=Player('2', False, [0x400000, 0x100000, 0x040000, 0x010000], DIR_DN)
    working = True

    while working:
        for p in [p1, p2]:
            Table.show_board()
            if not p.moving_items():
                print("{}: You lose...".format(p.name))
                quit()
            if p.human:
                while not p.ask():
                    pass
            p.move_item()


        
