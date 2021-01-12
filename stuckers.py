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

    def free_cell(item):
        b = sum(list(Table.items.values()))
        return True if (item & (Table.board ^ b)) > 0 else False

    def moveto(item, direction, increment):
        return item<<increment if direction == DIR_UP else item>>increment


class Player:

    pref_indx: int = 0
    pref_incr: int = DIR_RT

    def __init__(self, name, human, items, direction):
        self.name = name
        self.human = human
        self.items = items
        self.direction = direction
        self.upward = self.direction == DIR_UP
        self.homerow = 0x55 if self.upward else 0xAA00000000000000
        self.homecells = list(items)
        self.edgerow = 0xAA00000000000000 if self.upward else 0x55
        Table.items[self.name] = sum(self.items)

    def ask(self):
        n=0 
        n = input('{0}: Input index of item [{1}-{2}]:'.format(self.name, 0, len(self.items)-1))
        if n == 'q':
            return False
        if n.isdigit():
            self.pref_indx = int(n)
            d = input("{0}: Input direction (l | r):".format(self.name))
            if d == 'l':
                self.pref_incr = DIR_LT
            if d == 'r':
                self.pref_incr = DIR_RT
        return True

    def turn(self):
        c = self.items[self.pref_indx]<<self.pref_incr if self.direction == DIR_UP \
        else self.items[self.pref_indx]>>self.pref_incr 
        if Table.free_cell(c):
            if c & self.edgerow:
                self.items.pop(self.pref_indx)
                self.bifurcation()
            else:
                self.items[self.pref_indx] = c
            Table.items[self.name] = sum(self.items)
            return True
        else:
            print("{}: Wrong turn!".format(self.name))
            return False

    def bifurcation(self):
        if Table.free_cell(self.homerow):
            n = 2
            for i in self.homecells:
                if Table.free_cell(i):
                    self.items.append(i)
                    n-=1
                if n <= 0:
                    break
            return True
        return False

    def open_items_count(self):
        n = 0
        if not self.items:
            return 0
        for i in self.items:
            if Table.free_cell(i<<DIR_RT if self.upward else i>>DIR_RT) or \
                Table.free_cell(i<<DIR_LT if self.upward else i>>DIR_LT):
                n+=1
        return n

    def prepare(self):
        self.pref_indx = 0
        self.pref_incr = DIR_RT
        cur = 0
        cnt = 0
        for idx, item in enumerate(self.items):
            base_items, base_destinition = self.calculate(item)
            turns_count = len(list(set(base_items)))
            for incr in [DIR_LT, DIR_RT]:
                nt = Table.moveto(item, self.direction, incr)
                if Table.free_cell(nt):
                    ret, l = self.calculate(nt)
                    t = len(list(set(ret)))
                    if (turns_count-t) <= cnt:
                        self.pref_indx = idx
                        self.pref_incr = incr
                        cnt=(turns_count-t)
        print(self.pref_indx, self.pref_incr, cur, cnt)

    def calculate(self, item):
        l = 0
        ret = [item]
        if item & self.edgerow > 0:
            l = 1
        else:
            for d in [DIR_RT, DIR_LT]:
                c = item<<d if self.upward else item>>d
                if Table.free_cell(c):
                    _c, _l = self.calculate(c)
                    ret.extend(_c)
                    if _l:
                        l = _l+1
        return ret, l


def display(val):
    s = format(val, 'b').zfill(64)[::-1]
    out = ''
    for i in range(64, 0, -8):
        out = out + s[i - 8:i] + '\n'
    print(out)


if __name__ == "__main__":
    
    p1=Player('1', True, [0x1, 0x4, 0x10, 0x40], DIR_UP)
    p2=Player('2', False, [0x8000000000000000, 0x2000000000000000, 
             0x0800000000000000, 0x0200000000000000], DIR_DN)
 
#    p2=Player('2', False, [0x400000, 0x100000, 0x040000, 0x010000], DIR_DN)
    working = True

    while working:
        for p in [p1, p2]:
            if not p.open_items_count():
                print("{}: You lose...".format(p.name))
                quit()
            if p.human:
                Table.show_board()
                while not p.ask():
                    pass
            else:
                p.prepare()
            p.turn()


        
