#Descomponer un número
from math import*

numero = float(input("Introduce un número: "))

if (numero<9):
    unidad=numero
    unidad=str(unidad)
    print(unidad+"U")
elif (numero>9) and (numero<99):
    decenas=numero/10
    tmp=numero % 10
    unidades= tmp % 10
    a=int(unidades)
    b=int(decenas)
    x="D"
    z="U"
    print((str(b))+(str(x)),"+",(str(a))+(str(z)))

elif (numero>99) and (numero<999):
    centenas = numero / 100
    tmp = numero % 100
    decenas = tmp / 10
    unidades = tmp % 10
    a=int(unidades)
    b=int(decenas)
    c=int(centenas)
    x="U"
    y="D"
    z="C"
    print((str(c))+(str(z)),"+",(str(b))+(str(y)),"+",(str(a))+(str(x)))
elif (numero>999) and (numero<9999):
    umil = numero / 1000
    tmp = numero % 1000
    centenas = tmp / 100
    tmp = tmp % 100
    decenas = tmp / 10
    unidades = tmp % 10
    a=int(unidades)
    b=int(decenas)
    c=int(centenas)
    d=int(umil)
    x="U"
    y="D"
    z="C"
    p="M"
    print((str(d))+(str(p)),"+",(str(c))+(str(z)),"+",(str(b))+(str(y)),"+",(str(a))+(str(x)))