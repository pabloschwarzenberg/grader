import math
def area_triangulo(base, altura):
    return base * altura / 2

def area_rectangulo(base, altura):
    return base * altura

def area_rombo(diagonal1, diagonal2):
    return (diagonal1 * diagonal2) / 2

def area_circulo(radio):
    return math.pi * radio ** 2

print("Área de triángulo: ")
print(area_triangulo(2, 4))

print("Área de rectángulo: ")
print(area_rectangulo(8, 2))

print("Área de rombo: ")
print(area_rombo(23, 44))

print("Área de círculo: ")
print(area_circulo(7))
#numero perfecto
def numero_perfecto(a):
    suma = 0
    for n in range(1,a):
        if (a % (n) == 0):
            suma += (n)
    if a == suma:
        return True
    else:
        return False 
#jerigonzo
def jerigonzo(string):
    aux = ""
    for letra in string:
        aux += letra
        if letra.lower() in "aeiou":
            aux += "p" + letra
    return aux
    return string
#Encriptador ROT13
def rot13(cad):
  orig = 'abcdefghijklm'
  tgt = 'nopqrstuvwxyz'
  rotmapper = dict(zip(orig + tgt, tgt + orig))
  return ''.join(rotmapper.get(x.lower(), x) for x in cad)
    
           