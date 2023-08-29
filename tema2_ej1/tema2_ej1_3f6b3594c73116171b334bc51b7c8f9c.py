def area_triangulo(base,altura):
    return (base*altura)/2
def area_rectangulo(base,altura):
    return base*altura
def area_rombo(diagonal1,diagonal2):
    return (diagonal1*diagonal2)/2
def area_circulo(radio):
    from math import pi
    r2=radio**2
    return pi*r2

if __name__ == "__main__":
    eleccion=int(input("selecciona la figura para calcular el area: 1.triangulo 2.rectamgulo 3.rombo 4.circulo"))
    if eleccion==1:
      b=float(input("ingresa la base:"))
      a=float(input("ingresa la altura:"))
      print(area_triangulo(b, a))
    if eleccion==2:
      b = float(input("ingresa la base:"))
      a = float(input("ingresa la altura:"))
      print(area_rectangulo(b, a))
    if eleccion==3:
      d1=float(input("ingresa la diagonal 1: "))
      d2=float(input("ingresa la diagonal 2: "))
      print(area_rombo(d1, d2))
    if eleccion==4:
      r=float(input("ingresa el radio de el circulo: "))
      print(area_circulo(r))
           