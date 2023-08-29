from math import pi

#ESTIMADOS LES DEJO LOS DOS CODIGOS REALIZADOS YA QUE CUANDO DEJO EL MENU ME ARROJA ERROR Q NO PUEDE LEER EL INPUT PERO CUANDO LO DEJO SIN MENU 
#FUNCIONA BIEN 

#menu = 1

#while menu != 0:
# menu = int(input("Para calcular triangulo ingrese N° 1, para rectangulo N° 2, para rombo N° 3, para circulo N° 4, para Salir digite 0 :"))
 #if menu == 1:
       # print("Haz seleccionado triangulo")
       # base = float(input('Ingrese la base: '))
       # altura = float(input('Ingrese la altura: '))
       # def area_triangulo(base, altura):
           # return base * altura / 2
        #print("EL area del triangulo es: ", area_triangulo(base, altura))

 #elif menu == 2:
        #print("Haz seleccionado Rectangulo ")
        #base = float(input('Ingrese la base: '))
       # altura = float(input('Ingrese la altura: '))
       # def area_rectangulo(base, altura):
            #return base * altura
        #print("EL area del Rectangulo es: ",area_rectangulo(base, altura))

 #elif menu == 3:
      # print("Haz seleccionado Rombo")
      # diagonal1 = float(input('Ingrese la diagonal1: '))
     #  diagonal2 = float(input('Ingrese la diagonal2: '))
      # def area_rombo(diagonal1 ,diagonal2):
          #return diagonal1 * diagonal2 / 2
       #print("El area del Rombo es: ",area_rombo(diagonal1, diagonal2))

 #elif menu == 4:
        #print("Haz seleccionado circulo")
        #radio = float(input('Ingrese  el radio: '))
       # def area_circulo(radio):
          # return pi * radio ** 2
       # print("El area del circulo es: ",area_circulo(radio))

#if menu == 0:
   # print("Haz terminad el programa")


def area_rectangulo(base,altura):
    return base*altura
def area_circulo(radio):
    return pi*radio**2
def area_triangulo(base,altura):
    return (base*altura)/2
def area_rombo(diagonal1,diagonal2):
    return (diagonal1*diagonal2)/2

print(area_rectangulo(6,11))
print(area_circulo(5))
print(area_triangulo(11,18))
print(area_rombo(8,9))