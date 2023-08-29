import math

def area_triangulo(base,altura):
    solucion = (base * altura)/2
    return solucion

def area_rectangulo(base,altura):
    solucion = (base * altura)
    return solucion

def area_rombo(diagonal1,diagonal2):
    solucion = (diagonal1 * diagonal2)/2
    return solucion

def area_circulo(radio):
    solucion = ((math.pi) * (radio ** 2))
    return solucion

if __name__ == "__main__":
    base_tri = int(input("Ingrese la base del triangulo: "))
    altura_tri = int(input("Ingrese la altura del triangulo: "))
    base_rec = int(input("Ingrese la base del rectangulo: "))
    altura_rec = int(input("Ingrese la altura del rectangulo: "))
    diag1_rom = int(input("Ingrese la primera diagonal del rombo: "))
    diag2_rom = int(input("Ingrese la segunda diagonal del rombo: "))
    radio_circ = int(input("Ingrese el radio del circulo: "))
    
    print("El area del triangulo es: ",area_triangulo(base_tri,altura_tri))
    print("El area del rectangulo es: ",area_rectangulo(base_rec,altura_rec))
    print("El area del rombo es: ",area_rombo(diag1_rom,diag2_rom))
    print("El area del circulo es: ",area_circulo(radio_circ))