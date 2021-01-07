#checkers-stuckers
DIM=8

desc=0xaa55aa55aa55aa55
our=[1,4,16,64]
their=[0x8000000000000000, 0x2000000000000000,
       0x0800000000000000, 0x0200000000000000]

def display(val):
    s=format(val, 'b').zfill(64)[::-1]
    out = ''
    for i in range(64,0,-8):
        out=out + s[i-8:i] + '\n'
    print(out)

#def is_free_field(x, y, table=_table):
#def count_movies(table=_table):
    
def our_step():
    none              

def their_step():
    none

display(desc)
