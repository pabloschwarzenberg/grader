from math import pi

#lista = 1

#while lista != 0:
# lista = int(input("Al calcular un triangulo ingrese N1, para poder calcular un rectangulo N2, para poder calcular un rombo N3, para poder calcular un circulo N4, para poder abandonar presione 0 :"))
 #if lista == 1:
       # print("seleccionaste triangulo")
       # base = float(input('Ingresa la base: '))
       # altura = float(input('Ingresa la altura: '))
       # def area_triangulo(base, altura):
           # return base * altura / 2
        #print("EL area en el triangulo es: ", area_triangulo(base, altura))

 #elif lista == 2:
        #print("seleccionaste rectangulo ")
        #base = float(input('Ingresa la base: '))
       # altura = float(input('Ingresa la altura: '))
       # def area_rectangulo(base, altura):
            #return base * altura
        #print("EL area en el rectangulo es: ",area_rectangulo(base, altura))

 #elif lista == 3:
      # print("seleccionaste rombo")
      # diagonal1 = float(input('Ingresa la diagonal1: '))
     #  diagonal2 = float(input('Ingresa la diagonal2: '))
      # def area_rombo(diagonal1 ,diagonal2):
          #return diagonal1 * diagonal2 / 2
       #print("El area en el rombo es: ",area_rombo(diagonal1, diagonal2))

 #elif lista == 4:
        #print("seleccionaste circulo")
        #radio = float(input('Ingresa el radio: '))
       # def area_circulo(radio):
          # return pi * radio ** 2
       # print("El area en el circulo es: ",area_circulo(radio))

#if lista == 0:
   # print("terminaste el programa")


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