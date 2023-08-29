import math
def area_triangulo(base,altura):
    area = base*altura/2
    return area

def area_rectangulo(base,altura):
    area = base*altura
    return area

def area_rombo(diagonal1,diagonal2):
    area = diagonal1*diagonal2/2
    return area

def area_circulo(radio):
    area = math.pi*(radio**2)
    return area
    
print('''
Indique la figura de la cual desea calcular el área:
(1) triangulo
(2) rectangulo
(3) rombo
(4) circulo
''')

if __name__ == "__main__":
  figura = int(input('figura: '))

  if figura==1:
    base = int(input('Ingrese la base del triangulo: '))
    altura = int(input('Ingrese la altura del triangulo: '))
    print('El area del triangulo es',area_triangulo(base,altura))

  elif figura==2:
    base = int(input('Ingrese la base del rectangulo: '))
    altura = int(input('Ingrese la altura del rectangulo: '))
    print('El area del rectangulo es',area_rectangulo(base,altura))

  elif figura==3:
    diagonal1 = int(input('Ingrese una diagonal: '))
    diagonal2 = int(input('Ingrese la otra diagonal: '))
    print('El area del rombo es',area_rombo(diagonal1,diagonal2))

  elif figura==4:
    radio = int(input('Ingrese el radio: '))
    print('El area del circulo es',area_circulo(radio))
           