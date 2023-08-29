import math
def area_triangulo(base,altura):
    return (base*altura)/2

def area_rectangulo(base,altura):
    return base*altura

def area_rombo(diagonal1,diagonal2):
    return (diagonal1*diagonal2)/2

def area_circulo(radio):
    return (math.pi)*((radio)**2)

print("Bienvenido a la Calculadora Geométrica")
if __name__ == "__main__":
    a=input("¿Que area deseas calcular? ")
    if "triangulo" in a:
        b=eval(input("ingrese base "))
        c=eval(input("ingrese altura "))
        print("el área es "+str(area_triangulo(b,c)))
    if "rectangulo" in a:
        b=eval(input("ingrese base "))
        c=eval(input("ingrese altura "))
        print("el área es "+str(area_rectangulo(b,c)))
    if "rombo" in a:
        b=eval(input("ingrese diagonal 1 "))
        c=eval(input("ingrese diagonal 2 "))
        print("el área es "+str(area_rombo(b,c)))
    if "circulo" in a:
        b=eval(input("ingrese radio "))
        print("el área es "+str(area_circulo(b)))