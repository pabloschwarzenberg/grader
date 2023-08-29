import math
def area_triangulo (altura,base):
    areatriangulo= (base*altura)/2
    return(areatriangulo)

def area_rectangulo (altura,base):
    arearectangulo= altura*base
    return(arearectangulo)

def area_rombo (diagonal1, diagonal2):
    arearombo= (diagonal1*diagonal2)//2
    return(arearombo)

def area_circulo (radio):
    areacirculo= math.pi*(radio)**2
    return(areacirculo)