t=[['_','_','_'],
    ['_','_','_'],
    ['_','_','_']]
def mostrar_t(t):
    v=''
    v+=' '.join(t[0])+'\n'
    v+=' '.join(t[1])+'\n'
    v+=' '.join(t[2])+'\n'
    print(v)
def revisar_horizontal(t,fila):
    if t[fila][0]=='X' and t[fila][1]=='X' and t[fila][2]=='X':
        print('win cat')
        return -1
    elif t[fila][0]=='O' and t[fila][1]=='O' and t[fila][2]=='O':
        print('win mouse')
        return 1
    else:
        return 0

def revisar_vertical(t,columna):
    if t[0][columna]=='X' and t[1][columna]=='X' and t[2][columna]=='X':
        print('win cat')
        return -1
    elif t[0][columna]=='O' and t[1][columna]=='O' and t[2][columna]=='O':
        print('win mouse')
        return 1
    else:
        return 0

def revisar_diagonal_derecha(t):
    if t[0][0]=='X' and t[1][1]=='X' and t[2][2]=='X':
        print('win cat')
        return -1
    elif t[0][0]=='O' and t[1][1]=='O' and t[2][2]=='O':
        print('win mouse')
        return 1
    else:
        return 0

def revisar_diagonal_izquierda(t):
    if t[0][2]=='X' and t[1][1]=='X' and t[2][0]=='X':
        print('win cat')
        return -1
    elif t[0][2]=='O' and t[1][1]=='O' and t[0][2]=='O':
         print('win mouse')
         return 1
    else:
        return 0