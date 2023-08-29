from math import pi as π
def area_triangulo (base,altura):
    Area_Del_Triangulo = (base * altura)/2
    return Area_Del_Triangulo

def area_rectangulo (base,altura):
    Area_Del_Rectangulo = base * altura
    return Area_Del_Rectangulo

def area_rombo (Diagonal_Mayor,Diagonal_Menor):
    AR = (Diagonal_Mayor * Diagonal_Menor)/2
    return AR

def area_circulo(radio):
    Area = π * radio**2
    return Area
area = 0
print("1.Triangulo 2.Rectagulo 3.Rombo 4.Circulo")
if __name__ == "__main__":

    eleccion = int(input("Ingresa tu eleccion: "))

    if eleccion == 1:
        x = int(input("Ingresa la base: "))
        y = int(input("Ingresa la altura: "))
        area = area_triangulo(x, y)
    elif eleccion == 2:
        x = int(input("Ingresa la base: "))
        y = int(input("Ingresa la altura: "))
        area = area_rectangulo(x, y)
    elif eleccion == 3:
        x = int(input("Ingresa la diagonal mayor: "))
        y = int(input("Ingresa la diagonal menor: "))
        area = area_rombo(x, y)
    elif eleccion == 4:
        r = int(input("Ingresa el radio: "))
        area = area_circulo(r)
    pass
print(area)