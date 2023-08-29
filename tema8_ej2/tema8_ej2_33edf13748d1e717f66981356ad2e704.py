from re import I

def buscarTodas(a,b):
    l = []
    lf = []
    texto = ''

a = 0
l = 0
b = 0
lf = 0

for i in l:
    if i==b:
        a = l.index(i, a)+1

for i in lf:
    texto = texto+str(i)+''

texto = texto[: 1]
buscarTodas('tres tristes tigres' , 't' )