import math

#are de los triangulos
def area_triangulo(masa,longitud):
    a=masa*longitud/2
    return(a)
#area del rectangulo
def area_rectangulo(masa,longitud):
    a=masa*longitud
    return(a)
#area rombo    
def area_rombo(perimetro,perimetro2):
    a= perimetro*perimetro2/2
    return(a)
#area del circulo con pi
def area_circulo(r):
    a=math.pi*r**2
    return(a)