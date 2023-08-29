#Factores Primos
def descomponer_numeros(numero):
    factor=2
  
    while factor <= numero:
        if numero % factor == 0:
           print(factor)
           numero = numero // factor
        else:
           factor += 1
  
numero=int(input())

descomponer_numeros(numero)