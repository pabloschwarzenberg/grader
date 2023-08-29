import math
def area_triangulo(b,h):
    areatriangulo=((b*h)/2)
    return areatriangulo

def area_rectangulo(L1,L2):
    arearectangulo=(L1*L2)    
    return arearectangulo

def area_rombo(D,d):
    arearombo=(D*d/2)
    return arearombo

def area_circulo(r):
    areacirculo= (math.pi*r**2)
    return areacirculo

a=area_circulo(4)
print("area de circulo:",a)

b=area_rectangulo(10,6)
print("area de rectangulo:",b)

c=area_rombo(30,16)
print("area de rombo:",c)

d=area_circulo(4)
print("area de circulo:",d)
           