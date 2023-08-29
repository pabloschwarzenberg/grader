import math
def area_triangulo(base,altura):
    area_triangulo=(base*altura)/2
    return(area_triangulo)
    pass

def area_rectangulo(base,altura):
    area_rectangulo=(base*altura)
    return(area_rectangulo)
    pass

def area_rombo(diagonal1,diagonal2):
    area_rombo=(diagonal1*diagonal2)/2
    return(area_rombo)
    pass

def area_circulo(radio):
    area_circulo=(math.pi)*((radio)**2)
    return(area_circulo)
    pass

if __name__ == "__main__":
    print('opciones:')
    print('(1) Calcular Area Triangulo')
    print('(2) Calcular Area Rectangulo')
    print('(3) Calcular Area Rombo')
    print('(4) Calcular Area Circulo')
    seleccion=input('Ingrese opcion:')
    if seleccion=="1":
        base=int(input('Ingrese base:'))
        altura=int(input('Ingrese altura:'))
        print(area_triangulo(base,altura))
    elif seleccion=="2":
        base=int(input('Ingrese base:'))
        altura=int(input('Ingrese altura:'))
        print(area_rectangulo(base,altura))
    elif seleccion=="3":
        diagonal1=int(input('Ingrese diagonal1:'))
        diagonal2=int(input('Ingrese diagonal2:'))
        print(area_rombo(diagonal1,diagonal2))
    elif seleccion=="4":
        radio=int(input('Ingrese radio:'))          
        print(area_circulo(radio))   

    pass
           