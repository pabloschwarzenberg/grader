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

if __name__=="__main__":

  print('1)area triangulo')

  print('2)area rectangulo')

  print('3)area rombo')

  print('4)area circulo')



  opcion=int(input("digite opcion: "))

  if opcion==1:

    base=int(input("base: "))

    altura=int(input("altura: "))

    print("Area:",area_triangulo(base,altura))

   

  elif opcion==2:

    base=int(input("base: "))

    altura=int(input("altura: "))

    print("Area: ",area_rectangulo(base,altura))

   

  elif opcion==3:

    diagonal1=int(input("diagonal1: "))

    diagonal2=int(input("diagonal2: "))

    print("Area: ",area_rombo(diagonal1,diagonal2))

  elif opcion==4:

    radio=float(input("radio circulo: "))

           