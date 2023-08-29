from math import pi

def area_triangulo(base,altura):
    resultado_area_triangulo = (base*altura)/2
    return resultado_area_triangulo
    
def area_rectangulo(base , altura ):
    resultado_area_rectangulo = (base*altura)
    return resultado_area_rectangulo
    
def area_rombo(diagonal_1,diagonal_2):   
    resultado_area_rombo = (diagonal_1*diagonal_2)/2
    return resultado_area_rombo
  
def area_circulo(radio):
 resultado_area_circulo = (pi*radio**2)
 return resultado_area_circulo
 