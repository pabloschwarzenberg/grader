import math
def area_triangulo(base,altura):
   areatria = (base*altura)/2
   return areatria

def area_rectangulo(base,altura):
   arearect = base*altura
   return arearect

def area_rombo(diagonal1,diagonal2):
   arearom = (diagonal1*diagonal2)/2
   return arearom

def area_circulo(radio):
   areacir = (radio**2)*math.pi
   return areacir
           