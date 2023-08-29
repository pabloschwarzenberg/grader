from math import pi

def area_triangulo(b,h):
  area=b*h/2
  return area

def area_rectangulo(b,h):
  area=b*h
  return area

def area_rombo(d1,d2):
  area=d1*d2/2
  return area

def area_circulo(r):
  area=pi*r*r
  return area

if __name__ == "__main__":
  op=int(input("1. Área triángulo\n2. Área rectángulo\n3. Área rombo\n4. Área círculo\n¿Calcular...?"))
  if op==1:
    b=float(input("Insert base: "))
    h=float(input("Insert height: "))
    print(area_triangulo(b,h))
  if op==2:
    b=float(input("Insert base: "))
    h=float(input("Insert height: "))
    print(area_rectangulo(b,h))
  if op==3:
    d1=float(input("Insert first diagonal: "))
    d2=float(input("Insert second diagonal: "))
    print(area_rombo(d1,d2))
  if op==4:
    r=float(input("Insert radius: "))
    print(area_circulo(r))
  pass
           