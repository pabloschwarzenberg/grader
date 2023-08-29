from math import pi

def area_triangulo(base, altura):
   area = base*altura/2
   return area


def area_rectangulo(base, altura):
   area2 = base*altura
   return area2


def area_rombo(diagonal1, diagonal2):
   area3 = diagonal1*diagonal2/2
   return area3


def area_circulo(radio):
   area4 = (pi*radio**2)
   return area4