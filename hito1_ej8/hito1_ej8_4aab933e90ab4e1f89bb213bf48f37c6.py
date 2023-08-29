unidad = eval(input("ingrese su numero"))
unidaduwu =str(unidad)
if 10000>unidad>999:
    m = (unidaduwu[0])
    c = (unidaduwu[1])
    d = (unidaduwu[2])
    u = (unidaduwu[3])
if 1000>unidad>99:
    m = 0
    c = (unidaduwu[0])
    d = (unidaduwu[1])
    u = (unidaduwu[2])
if 100>unidad>9:
    m = 0
    c = 0
    d = (unidaduwu[0])
    u = (unidaduwu[1])
if 10>unidad:
    m=0
    c=0
    d=0
    u = unidaduwu[0]

print(m,end= '')
print("M +",end='')
print(c,end='')
print("C +",end='')
print(d,end='')
print("D +",end='')
print(u,end='')
print("U")
