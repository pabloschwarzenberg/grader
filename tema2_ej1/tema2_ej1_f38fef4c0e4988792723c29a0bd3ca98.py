import math
import sys
#El programa sí me funciona en idle shell y en pycharm

def area_triangulo(base,altura):
    area=base*altura/2
    print("El área del triángulo es: ",area)
    sys.exit(0)

def area_rectangulo(base,altura):
    area=base*altura/2
    print("El área del rectángulo es: ",area)
    sys.exit(0)

def area_rombo(diagonal1,diagonal2):
    area=diagonal1*diagonal2/2
    print("El área del rombo es: ",area)
    sys.exit(0)

def area_circulo(radio):
    area=(radio**2)*math.pi
    print("El área del círculo es: ",area)
    sys.exit(0)

if __name__ == "__main__":
    print("Calculadora Geométrica")
    opciones=0
    while opciones!=-1:
         opciones=int(input("Ingrese 1 para calcular el área de un triángulo, 2 para el rectángulo, 3 para el rombo, 4 para el círculo o -1 para salir: "))
         if opciones==1:
           altura=float(input("Ingrese una altura: "))
           base=float(input("Ingrese una base: "))
           a=area_triangulo(base,altura)
         elif opciones==2:
             altura=float(input("Ingrese una altura: "))
             base=float(input("Ingrese una base: "))
             a=area_rectangulo(base,altura)
         elif opciones==3:
             diagonal1=float(input("Ingrese una diagonal: "))
             diagonal2=float(input("Ingrese otra diagonal: "))
             a=area_rombo(diagonal1,diagonal2)
         elif opciones==4:
             radio=float(input("Ingrese un radio: "))
             a=area_circulo(radio)

           