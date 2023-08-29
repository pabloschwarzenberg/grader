#Factores Primos
#Definir la funcion factorizar_primos
def factorizar_primos(numero):
    divisor=2
#Si el numero es mayor que 1:
    while numero>1:
         if numero%divisor==0:
              print(divisor)
              numero=numero/divisor
         else:
              divisor=divisor+1
#Pedir al usuario ingresar el numero a factorizar              
numero=int(input())
factorizar_primos(numero)      