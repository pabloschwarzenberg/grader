# Calculadora Geométrica
import math 

def area_triangulo(base, altura):
    area_t = (base*altura)/2
    return area_t

def area_rectangulo(base, altura):
     area_rec = (base*altura)
     return area_rec

def area_rombo(diagonal1, diagonal2):
     area_rom = (diagonal1*diagonal2)/2
     return area_rom

def area_circulo(radio):
  area_circ = (radio**2)* math.pi
  return area_circ

           