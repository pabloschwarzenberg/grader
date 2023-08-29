import math

def area_triangulo(base,altura):
    z=0
    z= z+((base*altura)*0.5)
    return z
    

def area_rectangulo(base,altura):
    x=0
    x= x+(base*altura)
    return x

def area_rombo(diagonal1,diagonal2):
    c=0
    c= c+((diagonal1*diagonal2)*0.5)
    return c

def area_circulo(radio):
    v=0
    v= v+(math.pi*(radio**2))
    return v


if __name__ == "__main__":
    q=int(input('eliga una opción :(1)área triangulo (2)área rectangulo (3)área rombo (4)área circulo :'))
    if q==1:
        base=int(input('ingrese la base:'))
        altura=int(input('ingrese la altura:'))
        s=area_triangulo(base,altura)
        print('el area del triangulo es:',s,'metros cuadrados')
    if q==2:
        base=int(input('ingrese la base:'))
        altura=int(input('ingrese la altura:'))
        d=area_rectangulo(base,altura)
        print('el area del rectangulo es:',d,'metros cuadrados')
    if q==3:
       diagonal1=int(input('ingresa la diagonal 1:'))
       diagonal2=int(input('ingresa la diagonal 2:'))
       f=area_rombo(diagonal1,diagonal2)
       print('el area del rombo es:',f,'metros cuadrados')
    if q==4:
       radio=int(input('ingresa el radio:'))
       g=area_circulo(radio)
       print('el area del circulo es:',g,'metros cuadrados')
   