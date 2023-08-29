from math import*
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
  print('bienvenidos a la calculadora geométrica,presiona 1 para calcular el area del rectangulo')
  print('presiona 2 para el area del triangulo, 3 para el rombo y 4 para el círculo')
  a=float(input('ingrese un número'))
  if a==1:
    a=int(input('ingrese altura:'))
    b=int(input('ingrese la base: '))
    newarea=area_rectangulo(b,a)
    print(newarea)
  elif a==2:
    a=int(input('ingrese altura:'))
    b=int(input('ingrese la base: '))
    newarea=area_triangulo(b,a)
    print(newarea)
  elif a==3:
    a=int(input('ingrese diagonal1'))
    b=int(input('ingrese la diagonal2:'))
    newarea=area_rombo(a,b)
    print(newarea)
  elif a==4:
    a=int(input('ingrese radio:'))
    newarea=area_circulo(a)
    print(newarea)
 
           