from math import pi

def area_triangulo(base,altura):
    resultado=(base * altura)/2 
    pass
    return resultado

def area_rectangulo(base,altura):
    resultado=base * altura
    pass
    return resultado

def area_rombo(diagonal1,diagonal2):
    resultado=(diagonal1 * diagonal2)/2
    pass
    return resultado

def area_circulo(radio):
    resultado=pi*(radio**2)
    pass
    return resultado

if __name__ == "__main__":
    a = input("figura: ")
    a.lower()
    if a == "triangulo":
        base = int(input("ingrese la base: "))
        altura = int(input("ingrese la altura: "))
        resultado = area_triangulo(base, altura)
        print(resultado)
    elif a == "rectangulo":
        base = int(input("ingrese la base: "))
        altura = int(input("ingrese la altura: "))
        resultado =  area_rectangulo(base, altura)
        print(resultado)
    elif a == "rombo":
        diagonal1 = int(input("ingrese valor de la diagonal mayor: "))
        diagonal2 = int(input("ingrese valor de la diagonal menor: "))
        resultado = area_rombo(diagonal1, diagonal2)
        print(resultado)
    elif a == "circulo":
        radio = int(input("ingrese el valor del radio: "))
        resultado = area_circulo(radio)
        print(resultado)
    pass   