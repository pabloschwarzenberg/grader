from multiprocessing.spawn import import_main_path
def area_triangulo(base,altura):
    area_tri=((base*altura)/2)
    print(area_tri)
    return(area_tri)
def area_rectangulo(base,altura):
    area_rec=((base*altura))
    print(area_rec)
    return(area_rec)
def area_rombo(diagonal1,diagonal2):
    area_ro=((diagonal1*diagonal2)/2)
    print(area_ro)
    return(area_ro)
def area_circulo(radio):
    from math import pi
    area_cir=(((radio)**2)*pi)
    print(area_cir)
    return(area_cir)
