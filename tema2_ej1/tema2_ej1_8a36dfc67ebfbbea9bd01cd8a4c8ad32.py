import math

def area_triangulo(base,altura):
    area= base*altura/2
    return area

def area_rectangulo(base,altura):
    area= base*altura
    return area

def area_rombo(diago1,diago2):
    area=diago1*diago2/2
    return area

def area_circulo(radio):
    area=math.pi*(radio**2)
    return area

if __name__ == "__main__":
 n=int(input('Qué área deseas calcular?''\n''[1]=Triángulo''\n''[2]=Rectángulo''\n''[3]=Rombo''\n''[4]=Circulo''\n''[5]=Salir''\n'': '))
 if n==1:
     base=float(input('Ingrese la base: '))
     altura=float(input('Ingrese la altura: '))
     f=area_triangulo(base,altura)
     print('El área es:',f)
 if n==2:
     base=float(input('Ingrese la base: '))
     altura=float(input('Ingrese la altura: '))
     f=area_rectangulo(base,altura)
     print('El área es:',f)
 if n==3:
     diago1=float(input('Ingrese una diagonal: '))
     diago2=float(input('Ingrese la otra diagonal: '))
     f=area_rombo(diago1,diago2)
     print('El área es:',f)
 if n==4:
     radio=float(input('Ingrese la altura: '))
     f=area_circulo(radio)
     print('El área es:',f)
 if n==5:
     print('Adiós')

           