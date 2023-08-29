def areaTriangulo(base,altura):
    areaTotal = (float(base) * float(altura))/2
    return (f'El area del triangulo es: {areaTotal:.2f}')




def areaRectangulo(base,altura):
    areaTotal = (float(base) * float(altura))
    return (f'El area del rectangulo es: {areaTotal:.2f}')

    

def areaRombo(didagonalUno,diagonalDos):
    areaTotal = (float(didagonalUno) * float(diagonalDos))/2
    return (f'El Area total del Rombo es: {areaTotal:.2f}')

   

from math import pi


def areaCirculo(radio):
    areaTotal = (float(radio) ** 2) * pi
    return (f'El area del circulo es: {areaTotal:.2f}')

if __name__ == "__main__":

print('Calculadora Geometrica')
print('1. Area de un Triangulo')
print('2. Area de un recatngulo')
print('3. Area de un Rombo')
print('4. Area de un circulo')
operacion = int(input('Indica la operacion que deseas realizar: '))

if operacion == 1:
    altura = input('Ingrese la altura: ')
    base = input('Ingrese la Base: ')
    print(areaTriangulo(base,altura))
elif operacion == 2:
    altura = input('Ingrese la altura: ')
    base = input('Ingrese la Base: ')
    print(areaRectangulo(base,altura))
elif operacion == 3:
    diagonalUno = input('Ingrese la priera diagonal: ')
    diagonalDos = input('Ingrese la segunda diagonal: ')
    print(areaRombo(diagonalUno,diagonalDos))  
elif operacion == 4:
    radio = float(input('Ingrese el radio del circulo: '))
    print(areaCirculo(radio)) 

    
    
           