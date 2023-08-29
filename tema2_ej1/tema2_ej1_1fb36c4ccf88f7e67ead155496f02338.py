import math
def area_triangulo(base,altura):
    return (base*altura)/2

def area_rectangulo(base,altura):
    return base*altura

def area_rombo(diagonal1,diagonal2):
    return diagonal1*diagonal2/2

def area_circulo(radio):
    return math.pi*radio**2

if __name__ == "__main__":
    figura = ["triangulo","rectangulo","rombo","circulo"]
    while True:
        for k in range(4):
            print("({}) Calcular el area de un {:s}".format(k+1,figura[k]))
        print("(5) Salir.")
        op = input("Que quieres hacer?")
        if op == "1":
            base = float(input("Base: "))
            altura = float(input("Altura : ")) 
            print(area_triangulo(base,altura))
        elif op == "2":
            base = float(input("Base: "))
            altura = float(input("Altura : "))
            print(area_rectangulo(base,altura))
        elif op == "3":
            d1 = float(input("Diagonal 1: "))
            d2 = float(input("Diagonal 2: "))
            print(area_rombo(base,altura))
        elif op == "4":
            radio = float(input("Radio: "))
            print(area_circulo(radio))
        else:
            print("Hasta luego")
            break    
           