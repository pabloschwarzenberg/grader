import math
def area_triangulo(base,altura):
    return (base*altura)/2
    pass

def area_rectangulo(base,altura):
    return base*altura
    pass

def area_rombo(diagonal1,diagonal2):
    return (diagonal1*diagonal2)/2
    pass

def area_circulo(radio):
    return math.pi*(radio*radio)
    pass

if __name__ == "__main__":
    print("""
    1._ area_triangulo
    2._ area_reactangulo
    3._ area_rombo
    4._ area_circulo """)
    a = int(input("Ingrese el numero del menu del area de la figura que desea calcular"))
    if a == 1:
        base = float(input("Ingrese el valor de la base:"))
        altura = float(input("Ingrese el valor de la altura:"))
        print("El area del triangulo es: ",area_triangulo(base,altura))
    elif a == 2:
        base = float(input("Ingrese el valor de la base:"))
        altura = float(input("Ingrese el valor de la altura:"))
        print("El area del rectangulo es: ",area_rectangulo(base,altura))
    elif a == 3:
        diagonal1=float(input("Ingrese el valor de la diagonal1:"))
        diagonal2=float(input("Ingrese el valor de la diagonal2:"))
        print("El area del rombo es: ",area_rombo(diagonal1,diagonal2))
    elif a == 4:
        radio=float(input("Ingrese el valor del radio:"))
        print("El area del circulo es:",area_circulo(radio))
    else:
        print("Ingrese un numero valido")
    pass
           
