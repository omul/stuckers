#checkers-stuckers
DIM=8

_table=[[0 for i in range(DIM)] for j in range(DIM)]
_our=[(0, x,) for x in range(DIM) if x%2==0]
_their=[(DIM-1, x,) for x in range(DIM) if (DIM+x)%2!=0]

def print_table():
    for i in reversed(_table):
        print (i)

def is_free_field(x, y, table=_table):
    if x<0 or y<0 or x>DIM-1 or y>DIM-1:
        return False
    if (x+y)%2==0 and table[x][y]==0:
        return True
    else:
        return False

def count_movies(table=_table):
    if 
    
def our_step():
    counter=0
    for x,y in _our:
        if is_free_steps(x-1, y+1):
            count_movies()
        if is_free_steps(x+1, y+1):
            count_movies()
        counter+=1
        
      

def their_step():
    none


for i,j in _our:
    _table[i][j]=1

for i,j in _their:
    _table[i][j]=2


print_table()
