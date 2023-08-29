import math

def area_triangulo(base, altura):
    return (base*altura)/2

def area_rectangulo(base,altura):
    return base*altura

def area_rombo(diagonal1, diagoanl2):
    return (diagonal1*diagoanl2)/2

def area_circulo(radio):
    return math.pi*radio**2

if __name__ == '__main__':
    continuar = True
    while(continuar):
        print("")
        print("1) Calcular área de un triángulo")
        print("2) Calcular área de un rectángulo")
        print("3) Calcular área de un rombo")
        print("4) Calcular área de un círculo")
        print("0) Salir")
        print("-------------------------------")
        opcion = input("Elija una opción: ")
        if(opcion == "1"):
            print("Calcular área de un triángulo.")
            base = int(input("Ingrese base: "))
            altura = int(input("Ingrese altura: "))
            print("El área es ",area_triangulo(base,altura))
        elif(opcion == "2"):
            print("Calcular área de un rectángulo.")
            base = int(input("Ingrese base: "))
            altura = int(input("Ingrese altura: "))
            print("El área es ",area_rectangulo(base,altura))
        elif(opcion == "3"):
            print("Calcular área de un rombo.")
            d1 = int(input("Ingrese primera diagonal: "))
            d2 = int(input("Ingrese segunda diagonal: "))
            print("El área es ",area_rombo(d1,d2))
        elif(opcion == "4"):
            print("Calcular área de un circulo.")
            radio = int(input("Ingrese radio: "))
            print("El área es ",area_circulo(radio))
        elif(opcion == "0"):
            continuar = False
        else:
            print("Opción incorrecta")
    print("Chau!")   