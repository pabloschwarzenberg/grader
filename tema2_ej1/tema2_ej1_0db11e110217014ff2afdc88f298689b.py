import math
def area_triangulo(base,altura):
    area=(base*altura)/2
    return area
def area_rectangulo(base,altura):
    area=base*altura
    return area
def area_rombo(diagonal1,diagonal2):
    area=(diagonal1*diagonal2)/2
    return area
def area_circulo(radio):
    area=math.pi*(radio**2)
    return area
if __name__ == "__main__":
    print("Elige la figura geometrica a la que quieres calcular el area")
    print("1: Triangulo")
    print("2: Circulo")
    print("3: Rombo")
    print("4: Rectangulo")
    figura=int(input("Ingrese número de figura para calcular su area:"))
    if figura == 1:
        base = float(input("Introduzca valor de la base del triangulo:"))
        altura = float(input("Introduzca valor de la altura del triangulo:"))
        area = area_triangulo(base,altura)
        print ("El area del triangulo es: ",area)
    elif figura == 2:
        radio=float(input("Introduzca el valor del radio del circulo:"))
        area = area_circulo(radio)
        print("El area del circulo es: ",area)
    elif figura == 3:
        D = float(input("Introduzca el valor de la diagonal vertical del rombo:"))
        d = float(input("Introduzca el valor de la diagonal horizontal del rombo:"))
        area = area_rombo(D,d)
        print ("El area del rombo es: ",area)
    elif figura == 4:
        base=float(input("Introduzca el valor de la base del rectangulo:"))
        altura=float(input("Introduzca el valor de la altura del rectangulo:"))
        area = area_rectangulo(base,altura)
        print ("El area del rectángulo es: ",area)
   
    else:
        print("Funcion no valida") 
    
           