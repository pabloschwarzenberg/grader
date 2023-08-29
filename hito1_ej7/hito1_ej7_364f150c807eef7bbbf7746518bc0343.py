#Zodiaco
a='Aries'
b='Tauro'
c='Geminis'
d='Cancer'
e='Leo'
f='Virgo'
g='Libra'
h='Escorpio'
i='Sagitario'
j='Capricornio'
k='Acuario'
l='Piscis'
DIA= int(input('Dia: '))
MES= int(input('Mes: '))
if MES == 1:
    if DIA <= 19:
        print(j)
    elif DIA > 19:
        print(k)
elif MES == 2:
    if DIA <= 19:
        print(k)
    elif DIA > 19:
        print(l)
elif MES == 3:
    if DIA <= 21:
        print(l)
    elif DIA >21:
        print(a)
elif MES == 4:
    if DIA <= 20:
        print(a)
    elif DIA > 20:
        print(b)
elif MES == 5:
    if DIA <= 21:
        print(b)
    elif DIA > 21:
        print(c)
elif MES == 6:
    if DIA <= 21:
        print(c)
    elif DIA > 21:
        print(d)
elif MES == 7:
    if DIA <= 21:
        print(d)
    elif DIA > 21:
        print(e)
elif MES == 8:
    if DIA <= 23:
        print(e)
    elif DIA > 23:
        print(f)
elif MES == 9:
    if DIA <= 23:
        print(f)
    elif DIA > 23:
        print(g)
elif MES == 10:
    if DIA <= 23:
        print(g)
    elif DIA > 23:
        print(h)
elif MES == 11:
    if DIA <= 22:
        print(i)
    elif DIA > 22:
        print(j)
elif MES == 12:
    if DIA <= 22:
        print(j)
    elif DIA > 22:
        print(k)