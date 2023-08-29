def area_triangulo(base,altura):
    area = (base*altura)/2
    return area

def area_rectangulo(base,altura):
    area = base*altura
    return area

def area_rombo(diagonal1,diagonal2):
    area = (diagonal1*diagonal2)/2
    return area

def area_circulo(radio):
    import math
    area = math.pi*(radio**2)
    return area

if __name__ == "__main__":
    print("1.- TRIÁNGULO\n2.-CÍRCULO\n3.-CUADRADO\n4.-RECTÁNGULO")
    figura = int(input("Ingrese la opción correspondiente a la figura: "))
    if figura == 1:
        b = int(input("Ingrese el valor de la base del triángulo: "))
        h = int(input("Ingrese el valor de la altura del triángulo: "))
        print("El área del triángulo es: ",area_triangulo(b,h))
    elif figura == 2:
        r = int(input("Ingrese el radio del círculo: "))
        print("El área del círculo es: ",area_circulo(r))
    elif figura == 3:
        l = int(input("Ingrese el lado del rombo: "))
        print("El área del rombo es: ", area_rombo(l))
    else:
        l = int(input("Ingrese el largo del rectángulo: "))
        a = int(input("Ingrese el ancho del rectángulo: "))
        print("El área del rectángulo es: ", area_rectangulo(l,a))

           