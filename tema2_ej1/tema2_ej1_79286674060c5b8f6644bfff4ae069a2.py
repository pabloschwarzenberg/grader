def area_triangulo(base,altura):
    area=base*altura/2
    return area

def area_rectangulo(base,altura):
    area = base * altura
    return area

def area_rombo(diagonal1,diagonal2):
    area = diagonal1 * diagonal2 / 2
    return area

def area_circulo(radio):
    import math
    area=math.pi*radio**2
    return area

if __name__ == "__main__":
    print("1.Area de triangulo \n2.Area de rectangulo\n3.Area de rombo\n4.Area de circulo" )
    eleccion=input("Que desea calcular?")
    if eleccion =="1":
        print(area_triangulo(float(input("Ingresa base: ")),float(input("Ingresa altura: "))))
    elif eleccion=="2":
        print(area_rectangulo(float(input("Ingresa base: ")), float(input("Ingresa altura: "))))
    elif eleccion=="3":
        print(area_rombo(float(input("Ingresa diagonal 1: ")), float(input("Ingresa diagonal 2: "))))
    elif eleccion=="4":
        print(area_circulo(float(input("Ingresa radio"))))
    else:
        print("Respuesta invalida")