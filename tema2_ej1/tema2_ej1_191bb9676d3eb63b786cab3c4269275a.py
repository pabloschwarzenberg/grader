import math
def area_triangulo(base,altura):
    a=base*altura/2
    return a

def area_rectangulo(base2,altura2):
    b=base2*altura2
    return b

def area_rombo(diagonal1,diagonal2):
    c=diagonal1*diagonal2/2
    return c

def area_circulo(radio):
    pi=math.pi
    d=pi*radio*radio
    return d
if __name__ == "__main__":
   print(" Para calcular el area de un triangulo presione 1 \n Para calcular el area de un rectangulo presiona 2 \n Para calcular el area de un rombo presione 3 \n Para calcular el area de un cirulo presione 4")
   opcion=int(input("Ingrese su opcion "))
   if opcion==1:
      base=int(input("ingrese el valor de la base "))
      altura=int(input("Ingrese el valor de la altura "))
      print (area_triangulo(base,altura))
   
   elif opcion==2:
       base2=int(input("ingrese el valor de la base "))
       altura2=int(input("Ingrese el valor de la altura "))
       print(area_rectangulo(base2,altura2))
    
   elif opcion==3:
       diagonal1=int(input("Ingrese el valor de la diagonal 1 del rombo "))
       diagonal2=int(input("Ingrese el valor de la diagonal 2 del rombo "))
       print(area_rombo(diagonal1,diagonal2))

   elif opcion==4:
       radio=int(input("Ingrese el radio de la circunferencia "))
       print(area_circulo(radio))


