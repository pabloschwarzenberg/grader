from math import pi

def area_triangulo(base,altura):
    area=(base*altura)/2
    return area

def area_rectangulo(base,altura):
    area=base*altura
    return area

def area_rombo(diagonal1,diagonal2):
    area=(diagonal1*diagonal2)/2
    return area

def area_circulo(radio):
    area=pi*(radio**2)
    return area

if __name__ == "__main__":
  opcion=eval(input('triangulo(1), rectangulo(2), rombo(3), circulo(4)'))
  if opcion==1:
    base=eval(input('base: '))
    altura=eval(input('altura: '))
    print(area_triangulo(base,altura))
  if opcion==2:
    base=eval(input('base: '))
    altura=eval(input('altura: '))
    print(area_rectangulo(base,altura))
  if opcion==3:
    diagonal1=eval(input('diagonal1: '))
    diagonal2=eval(input('diagonal2: '))
    print(area_rombo(diagonal1,diagonal2))
  if opcion==4:
    radio=eval(input('radio: '))
    print(area_circulo(radio))