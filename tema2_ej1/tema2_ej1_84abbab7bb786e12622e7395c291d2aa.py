def area_triangulo(base,altura):
    base=int(base)
    altura=int(altura)
    area=base*altura*0.5
    return area
    pass

def area_rectangulo(base,altura):
    base=int(base)
    altura=int(altura)
    area=base*altura
    return area
    pass

def area_rombo(diagonal1,diagonal2):
    diagonal1=int(diagonal1)
    diagonal2=int(diagonal2)
    area=diagonal1*diagonal2*0.5
    return area
    pass

def area_circulo(radio):
    radio=int(radio)
    from math import pi
    area=pi*radio**2
    return area
    pass

if __name__ == "__main__":
    figura=input('Ingrese la figura')
    if figura=='circulo':
        radio=input('ingrese radio')
        area_circulo(radio)
    if figura=='rombo':
        diagonal1=input('ingrese diagonal 1')
        diagonal2=input('ahora la 2')
        area_rombo(diagonal1,diagonal2)

    if figura=='rectangulo':
        base=input('base')
        altura=input('altura')
        area_rectangulo(base,altura)
           

    if figura=='triangulo':
        base=input('base')
        altura=input('altura')
        area_triangulo(base,altura)
            
    pass