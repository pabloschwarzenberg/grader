import math
def area_triangulo(base,altura):
    resultado1=(base*altura/2)
    return resultado1

def area_rectangulo(base,altura):
    resultado2=(base*altura)
    return resultado2
   
def area_rombo(diagonalmayor,diagonalmenor):
    resultado3=(diagonalmayor*diagonalmenor/2)
    return resultado3

def area_circulo(radio):
    resultado4=(math.pi*radio**2)
    return resultado4

resultado1=area_triangulo(3,4)
print (resultado1)

resultado2=area_rectangulo(3,4)
print (resultado2)

resultado3=area_rombo(3,4)
print (resultado3)

resultado4=area_circulo(3)
print (resultado4)

           