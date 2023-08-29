import math
def area_triangulo(base,altura):
    areatriangulo=(altura*base)/2
    return(areatriangulo)

def area_rectangulo(base,altura):
    arearectangulo=(altura*base)
    return(arearectangulo)

def area_rombo(diagonal1,diagonal2):
    arearombo=(diagonal1*diagonal2)/2
    return(arearombo)

def area_circulo(radio):
    areacirculo= (math.pi)*radio*radio
    return(areacirculo)
    
if __name__ == "__main__":
    pass
           