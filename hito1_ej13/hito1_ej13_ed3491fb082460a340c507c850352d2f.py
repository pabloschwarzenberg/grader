#Factores Primos
def funcion(numero):
   if numero < 2:
      print(0)
   for x in range(2,numero):
      a = numero % x
      if a != 0:
         print(a)
      
ingresa = int(input("Ingresa un numero"))
print(funcion(ingresa))