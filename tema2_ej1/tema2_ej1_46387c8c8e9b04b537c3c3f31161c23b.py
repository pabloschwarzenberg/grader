def area_triangulo(base,altura):
    a = (base*altura)/2
    return a
    pass
    
def area_rectangulo(base,altura):
    a2 = base*altura
    return a2 
    pass

def area_rombo(diagonal1,diagonal2):
    a3 = (diagonal1 * diagonal2)/2
    return a3
    pass

def area_circulo(radio):
    a4 = (radio**2)*3.14159265358979323846
    return a4
    pass

def eleccion(m):
    print("1. Triangulo")
    print("2. Rectangulo")
    print("3. Rombo")
    print("4. Circulo")
    m = int(input("Elija Opcion: "))
    if m == 1:
        base = int(input("Base de triangulo: "))
        altura = int(input("Altura de triangulo: "))
        print(area_triangulo)
    if m == 2:
        base = int(input("Base de rectangulo: "))
        altura = int(input("Altura de rectangulo: "))
        print(area_rectangulo)
    if m == 3:
        diagonal1 = int(input("Diagonal 1 de Rombo: "))
        diagonal2 = int(input("Diagonal 2 de Rombo: "))
        print(area_rombo)
    if m == 4:
        radio = int(input("Radio de Circulo: "))
        print(area_circulo)


