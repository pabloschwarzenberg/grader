# Importaciones
import math

# Definicion de area de un triangulo
def area_triangulo(b,h):
 area = b * h/2 # BASE POR ALTURA DIVIDIDO EN 2
 return area

# Definicion de area de un rectangulo
def area_rectangulo(b,h):
 area = b * h # BASE POR ALTURA
 return area
 
# Definicion de area de un rombo
def area_rombo(d1,d2):
 area = (d1*d2)/2 # DIAGONAL 1 * DIAGONAL 2
 return area
 
# Definicion de area de un circulo 
def area_circulo(r):
 area = math.pi*r**2 # PI * R AL CUADRADO
 return area   