import math
def area_triangulo(base,altura):
    area=altura*base/2
    return area

def area_rectangulo(base,altura):
    area=base*altura
    return area

def area_rombo(diagonal1,diagonal2):
    area= diagonal1*diagonal2/2
    return area

def area_circulo(radio):
    area=radio**2*math.pi
    return area


'''JERIGONZO'''
def jerigonzo(string):
    convertido = []
    for palabra in string:
        for letra in palabra:
            if letra in "aeiouAEIOU":
                letra = letra + "p"+ letra
            convertido.append(letra)
    convertido = "".join(convertido)
    return convertido
