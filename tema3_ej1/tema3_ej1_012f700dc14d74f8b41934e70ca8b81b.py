# completa el código de la función

def suma_divisores(numero):
   suma = 0
   for i in range int(1, numero):
       if numero % i == 0:
           suma += i
   return suma


numero = ("Ingresa el número:")
("La suma es de sus divisores es:")
(suma_divisores(numero))          