import math
def area_triangulo(base,altura):
    area=(base*altura)/2
    return area

def area_rectangulo(base,altura):
    area=base*altura
    return area

def area_rombo(diagonal1,diagonal2):
    area=(diagonal1*diagonal2)/2
    return area

def area_circulo(radio):
    area=(radio**2)*math.pi
    return area

if __name__=="__main__":
    main=int(input("Deseas calcular el área de:\n- Triángulo(1)\n- Rectángulo(2)\n- Rombo(3)\n- Círculo(4)\nIngresa el número de tu respuesta: "))

    if main==1:
        base=int(input("Base: "))
        altura=int(input("Altura: "))
        print("El área del Triángulo es",area_triangulo(base,altura))

    if main==2:
        base=int(input("Base: "))
        altura=int(input("Altura: "))
        print("El área del Rectángulo es",area_rectangulo(base,altura))

    if main==3:
        d1=int(input("Diagonal 1: "))
        d2=int(input("Diagonal 2: "))
        print("El área del Rombo es",area_rombo(d1,d2))

    if main==4:
        r=int(input("Radio: "))
        print("El área del Círculo es",area_circulo(r))