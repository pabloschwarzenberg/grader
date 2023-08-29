from math import pi
def area_triangulo(base, altura):
    ecuacion=(base*altura)/2
    return ecuacion


def area_rectangulo(base, altura):
    formula=base*altura
    return formula



def area_rombo(diagonal1, diagonal2):
    area=(diagonal1*diagonal2)/2
    return area



def area_circulo(radio):
    Acirculo=(pi)*(radio)**2
    return Acirculo



if __name__ == "__main__":
    print("que area quiere calcular: \n area triangulo(t) \n area rectangulo(r) \n area rombo(ro) \n area circulo(c)")
    o=input("que area quiere calcular: ")
    o=o.lower()
    if o=="t":
        b=int(input("base: "))
        a=int(input("altura: "))
        r=area_triangulo(a,b)
        print(r)
    elif o=="r":
        b = int(input("base: "))
        a = int(input("altura: "))
        r=area_rectangulo(a,b)
        print(r)
    elif o=="ro":
        b = int(input("diagonal1: "))
        a = int(input("diagonal2: "))
        r=area_rombo(a,b)
        print(r)
    elif o=="c":
        a=float(input("radio: "))
        r=area_circulo(a)
        print(r)
           