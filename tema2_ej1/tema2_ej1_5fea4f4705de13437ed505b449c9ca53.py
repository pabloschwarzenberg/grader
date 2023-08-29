def area_triangulo(base, altura):
    return base*altura/2
if __name__=="__main__":
    a=float(input('Ingrese la alturadel triangulo en metros: '))
    b=float(input('Ingrese la base del triangulo en metros: '))
    print(area_triangulo(base=b, altura=a))
pass
def area_rectangulo(base, altura):
    return base*altura
if __name__=="__main__":
    a=float(input('Ingrese la altura del rectangulo en metros: '))
    b=float(input('Ingrese la base del rectangulo en metros: '))
    print(area_rectangulo(base=b, altura=a))
pass
def area_rombo(diagonal1, diagonal2):
    return diagonal1*diagonal2/2
if __name__=="__main__":
    a=float(input('Ingrese la diagonal1 del rombo en metros: '))
    b=float(input('Ingrese la diagonal2 del rombo en metros: '))
    print(area_rombo(diagonal1=a, diagonal2=b))
pass
import math
def area_circulo(radio):
    return math.pi*(radio**2)
if __name__=="__main__":
    r=float(input('Ingrese el radio en metros: '))
    print(area_circulo(radio=r))
pass 