import math

def area_triangulo(base,altura):
    area=base*altura/2
    return area
def area_rectangulo(base,altura):
    area=base*altura
    return area
def area_rombo(diagonal1,diagonal2):
    area=diagonal1*diagonal2/2
    return area
def area_circulo(radio):
    area=radio**2*math.pi
    return area
    
if __name__ == "__main__":
    figura=str(input("De que figura deseas calcular el area?(triangulo/rectangulo/rombo/circulo)"))
    figura=adaptar(figura)
    while figura not in valido:
        print("Respuesta no valida.")
        figura=input("De que figura deseas calcular el area?(triangulo/rectangulo/rombo/circulo)")
        figura=adaptar(figura)
    if figura=="triangulo":
        base=float(input("Ingrese la base del triangulo: "))
        altura=float(input("Ingrese la altura del triangulo: "))
        print("El area del triangulo es: ",area_triangulo(base,altura))
    elif figura=="rectangulo":
        base=float(input("Ingrese la base del rectangulo: "))
        altura=float(input("Ingrese la altura del rectangulo: "))
        print("El area del rectangulo es: ",area_rectangulo(base,altura))
    elif figura=="rombo":
        diagonal1=float(input("Ingrese la primera diagonal del rombo: "))
        diagonal2=float(input("Ingrese la segunda diagonal del rombo: "))
        print("El area del rombo es: ",area_rombo(diagonal1,diagonal2))
    elif figura=="circulo":
        radio=float(input("Ingrese el radio del circulo: "))
        print("El area del circulo es: ",area_circulo(radio))


           