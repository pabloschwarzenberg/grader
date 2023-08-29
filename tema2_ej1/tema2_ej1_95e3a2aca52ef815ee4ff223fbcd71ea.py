def area_triangulo(base,altura):
    area = (base*altura)/2
    return area

def area_rectangulo(base,altura):
    area=base*altura
    return area

def area_rombo(diagonal1,diagonal2):
    area = (diagonal1*diagonal2)/2
    return area

def area_circulo(radio):
    from math import pi
    area = pi*(radio**2)
    return area

if __name__ == "__main__":
    opciones = print("1 = triángulo, 2=rectángulo, 3=rombo, 4=círculo")
    categoria = int(input("El area de qué figura desea conocer?"))
    if categoria == 1:
        base = int(input("Ingrese la base: "))
        altura = int(input("Ingrese la altura: "))
        print(triangulo = area_triangulo(base,altura))
    elif categoria == 2:
        base = int(input("Ingrese la base: "))
        altura = int(input("Ingrese la altura: "))    
        print(rectangulo = area_rectangulo(base,altura))
    elif categoria == 3:
        diagonal1 = int(input("Ingrese la diagonal 1: "))
        diagonal2 = int(input("Ingrese la diagonal 2: "))
        print(rombo = area_rombo(diagonal1,diagonal2))
    elif categoria == 4:
        radio = int(input("Ingrese el radio: "))
        print(circulo = area_circulo(radio))
        
        
    
           