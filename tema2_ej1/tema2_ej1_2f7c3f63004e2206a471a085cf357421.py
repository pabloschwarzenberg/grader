from math import pi

def area_triangulo(base, altura):
    area = (base*altura)/2
    return area

def area_rectangulo(base, altura):
    area = base*altura
    return area

def area_rombo(diagonal1, diagonal2):
    area = (diagonal1*diagonal2)/2
    return area

def area_circulo(radio):
    area = (radio**2)*pi
    return area
   
def escoger():
    elecciones = ["CIRCULO", "RECTANGULO", "ROMBO", "TRIANGULO"]
    escoge = input("Ingrése la figura para calcular su área: ").upper()
    if escoge in elecciones:
        if escoge == elecciones[0]:
            radio = float(input("ingrese la medida del radio: "))
            area = print(area_circulo(radio))
            return area
        if escoge == elecciones[1]:
            base = float(input("ingrese la medida de la base: "))
            altura = float(input("ingrese la medida de la altura: "))
            area = print(area_rectangulo(base, altura))
            return area
        if escoge == elecciones[2]:
            diagonal1 = float(input("ingrese la medida de una de las diagonales: "))
            diagonal2 = float(input("ingrese la medida de la otra diagonal: "))
            area = print(area_rombo(diagonal1, diagonal2))
            return area
        if escoge == elecciones[3]:
            base = float(input("ingrese la medida de la base: "))
            altura = float(input("ingrese la medida de la altura: "))
            area = print(area_triangulo(base, altura))
            return area