import math
math.pi

#SELECCIONADOR DE FIGURA GEOMETRICA

print("(1) A del Triángulo /n (2) A del Rectángulo /n (3) A del Rombo /n (4) A del Círculo")


#Opcion número 1 (Triángulo):

def area_triangulo(base,altura):
    operacion = (base * altura) /2
    return operacion
    pass
    
#Opcion número 2 (Rectángulo):

def area_rectangulo(base,altura):
    operacion = (base * altura)
    return operacion
    pass

def area_rombo(diagonal1,diagonal2):
    operacion = (diagonal1 * diagonal2) /2
    return operacion
    pass

def area_circulo(radio):
    operacion = (radio*radio*math.pi)
    return operacion
    pass
           