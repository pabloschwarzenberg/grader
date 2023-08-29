import math
def area_triangulo(base,altura):
    n=(base*altura)/2
    return n
    pass
def area_rectangulo(base,altura):
    n=(base*altura)
    return n 
    pass

def area_rombo(diagonal1,diagonal2):
    n=(diagonal1*diagonal2)/2
    return n 
    pass

def area_circulo(radio):
    n=(math.pi)*(radio**2)
    return n
    pass

if __name__ == "__main__":
    m=input("1 para area triangulo, 2 para area rectangulo, 3 para area rombo, 4 para area circulo")
    if m==1:
      base=input("base")
      altura=input("altura")
      print(str(area_triangulo(base,altura)))
    elif m==2:
      base=input("base")
      altura=input("altura")
      print(str(area_rectangulo(base,altura)))
    elif m==3:
      base=input("diagonal1")
      altura=input("diagonal2")
      print(str(area_rombo(base,altura)))
    elif m==2:
      base=input("radio")
      print(str(area_circulo(base)))
    pass
           