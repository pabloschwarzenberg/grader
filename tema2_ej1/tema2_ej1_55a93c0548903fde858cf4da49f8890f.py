import math 

def area_triangulo(base,altura):
    area_tria = (base*altura)/2
    return area_tria
    pass

def area_rectangulo(base,altura):
    area_rec = base*altura
    return area_rec
    pass

def area_rombo(diagonal1,diagonal2):
    area_rom=(diagonal1*diagonal2)/2
    return area_rom
    pass

def area_circulo(radio):
    area_cir = math.pi*radio*radio
    return area_cir
    pass

if __name__ == "__main__":
    print("Escriba el numero de la opcion que desea usar:")
    print("Area de un triangulo, opcion 1")
    print("Area de un rectangulo, opcion 2")
    print("Area de un rombo, opcion 3")
    print("Area de un circulo, opcion 4")
    pregunta = int(input(" "))
    if pregunta == 1:
        base = int(input("Ingrese base del triangulo: "))
        altura = int(input("Ingrese altura del triangulo: "))
        area = area_triangulo(base,altura)
        print(area) 
    elif pregunta == 2:
        base = int(input("Ingrese base del rectangulo: "))
        altura = int(input("Ingrese altura del rectangulo: "))
        area = area_rectangulo(base,altura)
    elif pregunta == 3:
        diagonal1 = int(input("Ingrese la primera diagonal del rombo: "))
        diagonal2 = int(input("Ingrese la segunda diagonal del rombo: "))     
        area = area_rombo(diagonal1,diagonal2)
    elif pregunta == 4:
        radio = int(input("Ingrese el radio del circulo: "))
        area = area_circulo(radio)