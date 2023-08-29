import math

def Menu():

  print ("""************
Calculadora
************
Menu
1) Area rectangulo
2) Area triangulo
3) Area rombo
4) Area circulo""")

def area_triangulo(base,altura):
    at = (base*altura)/2
    return at

def area_rectangulo(base,altura):
    ar = base*altura
    return ar

def area_rombo(diagonal1,diagonal2):
    arb = (diagonal1*diagonal2)/2
    return arb

def area_circulo(radio):
    ac = math.pi*radio*radio
    return ac
           