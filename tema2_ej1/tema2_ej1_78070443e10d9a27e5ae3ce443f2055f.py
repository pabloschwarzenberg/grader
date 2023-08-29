import math

def calcular_area_rectangulo(base, altura):
    return base * altura

def calcular_area_triangulo(base, altura):
    return 0.5 * base * altura

def calcular_area_rombo(diagonal_mayor, diagonal_menor):
    return 0.5 * diagonal_mayor * diagonal_menor

def calcular_area_circulo(radio):
    return math.pi * radio ** 2
    
  

base=int(input("Ingrese numero: "))
altura=int(input("ingrese numero: " ))
calcular_area_rectangulo(base, altura)


base=int(input("Ingrese numero: "))
altura=int(input("ingrese numero: " ))
calcular_area_triangulo(base, altura)

diagonal_mayor=int(input("Ingrese numero: "))
diagonal_menor=int(input("Ingrese numero: "))
calcular_area_rombo(diagonal_mayor, diagonal_menor)

radio=int(input("Ingrese numero: "))
calcular_area_circulo(radio)
 
  



           