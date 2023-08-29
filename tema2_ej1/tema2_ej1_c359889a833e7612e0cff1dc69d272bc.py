import math
def area_triangulo(basetr,alturatr):
    areatr=(basetr*alturatr)/2
    return areatr
def area_rectangulo(basere,alturare):
    areare=basere*alturare
    return areare
def area_rombo(diagonal1,diagonal2):
    arearo=diagonal1*diagonal2/2
    return arearo
def area_circulo(radio):
    areacir=math.pi*(radio**2)
    return areacir
if __name__=="__main__":
    figura=int(input("1. Triángulo. \n2. Rectángulo. \n3. Rombo. \n4. Círculo. \nIngrese un número de acuerdo a la figura que quiere calcular: "))
    if figura==1:
        if __name__=="__main__":
            b=int(input("Ingrese la base del triángulo: "))
        if __name__=="__main__":
            a=int(input("Ingrese la altura del triángulo: "))
        area=int(area_triangulo(b,a))
        print("El área del triángulo es: ",area)
    elif figura==2:
        if __name__=="__main__":
            b=int(input("Ingrese la base del rectángulo: "))
        if __name__=="__main__":
            a=int(input("Ingrese la altura del rectangulo: "))
        area=int(area_rectangulo(b,a))
        print("El área del rectángulo es: ",area)
    elif figura==3:
        if __name__=="__main__":
            d1=int(input("Ingrese la diagonal 1 del rombo: "))
        if __name__=="__main__":
            d2=int(input("Ingrese la diagonal 2 del rombo: "))
        area=int(area_rombo(d1,d2))
        print("El área del rombo es: ",area)
    elif figura==4:
        if __name__=="__main__":
            r=int(input("Ingrese el radio del círculo: "))
        area=(area_circulo(r))
        print("El área del círculo es: ",area)
    else:
        print("El número no es válido.")