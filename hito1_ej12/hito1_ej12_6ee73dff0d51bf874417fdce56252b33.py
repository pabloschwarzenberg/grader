#Juego adivina mi número
from random import randint

numero=randint(1,20)
intentos=5



while(intentos!=0):
 valor=int(input("valor entre 1 y 20 "))

 if(valor<numero):
    intentos=intentos-1
    print("Mi número es mas grande")

 if(valor>numero):
     intentos=intentos-1
     print("Mi número es mas pequeño")

 if(valor==numero):
    print("Adivinaste, mi número era ", numero)