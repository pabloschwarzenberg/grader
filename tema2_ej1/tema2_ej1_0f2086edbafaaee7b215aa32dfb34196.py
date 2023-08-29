import math 
def area_triangulo(base,altura):
    area=base*altura/2
    return area

def area_rectangulo(base,altura):
    area=base*altura
    return area
    

def area_rombo(diagonal1,diagonal2):
    area=diagonal1*diagonal2/2
    return area

def area_circulo(radio):
    area=math.pi*(radio**2)
    return area

if __name__ == "__main__":
    numero=int(input("1 or 2 or 3 or 4:"))
    if numero==1:
        baset=int(input("base t"))
        alturat=int(input("altura t"))
        at=int(area_triangulo(baset,alturat))
        print(at)
    elif numero==2:
        baser=int(input("base r"))
        alturar=int(input("altura r"))
        ar=int(area_rectangulo(baser,alturar))
        print(ar)
    elif numero==3:
        diagonal1=int(input("diagonal1:"))
        diagonal2=int(input("diagonal2:"))
        d12=int(area_rombo(diagonal1,diagonal2))
        print(d12)
    elif numero==4:
        radio=int(input("radio:"))
        r=int(area_circulo(radio))
        print(r)