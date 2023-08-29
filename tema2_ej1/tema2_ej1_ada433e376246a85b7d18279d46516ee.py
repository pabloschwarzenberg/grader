import math
menu=0
def area_triangulo(base1, altura1):
    area1=(base1*altura1)/2
    return area1
def area_rectangulo(base2, altura2):
    area2=base2*altura2
    return area2
def area_rombo(diagonal1, diagonal2):
    area3=diagonal1*diagonal2/2
    return area3
def area_circulo(radio):
    area4=math.pi*(radio*radio)
    return area4

if menu==1:
    area_triangulo(base1,altura1)
if menu==2:
    area_rectangulo(base2,altura2)
if menu==3:
    area_rombo(diagonal1,diagonal2)
if menu==4:
    area_circulo(radio)
           