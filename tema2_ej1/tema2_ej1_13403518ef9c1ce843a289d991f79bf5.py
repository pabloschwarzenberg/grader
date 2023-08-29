import math
def area_triangulo(base,altura):
    area =(base*altura)/2.0
    print("El área del triángulo es de: ", area)
    return area

def area_rectangulo(base,altura):
    area = base*altura
    print("El área del rectángulo es de: ", area)
    return area

def area_rombo(diagonal1,diagonal2):
    area = (diagonal1*diagonal2)/2.0
    print("El área del rombo es de: ", area)
    return area

def area_circulo(radio):
    area = math.pi*radio*radio
    print("El área del circulo es de: ", area)
    return area

if __name__ == "__main__":
    print("Bienvenido al programa para cálcular áreas!")
    print("Si quiere calcular el área de un triángulo, aprete 0")
    print("Si quiere calcular el área de un rectángulo, aprete 1")
    print("Si quiere calcular el área de un rombo, aprete 2")
    print("Si quiere calcular el área de un círculo, aprete 3")
    opcion= int(input(" "))
    if opcion ==0:
        altura = int(input("Cuanto mide la altura del triángulo?"))
        base = int(input("Cuanto mide la base del triángulo?")) 
        area_triangulo(base,altura)
    elif opcion ==1:
        altura = int(input("Cuanto mide la altura del rectángulo?"))
        base = int(input("Cuanto mide la base del rectángulo?")) 
        area_rectangulo(base,altura)     
    elif opcion ==2:
        d1 = int(input("Cuanto mide la diagonal 1 del rombo?"))
        d2 = int(input("Cuanto mide la diagonal 2 del rombo?")) 
        area_rombo(d1,d2) 
    elif opcion ==3:
        radio = int(input("Cuanto mide el radio del círculo?"))
        area_circulo(radio)  
    pass
           
           