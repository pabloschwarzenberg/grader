#Factores Primos
def descomponer_numero(numero):
  for i in range(2,numero+1):
    while numero%i==0:
      print(i)
      numero/=i
numero=int(input('ingrese un numero:'))
d=descomponer_numero(numero)