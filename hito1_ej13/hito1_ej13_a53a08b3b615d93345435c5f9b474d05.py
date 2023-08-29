#Factores Primos
def descomp_factores_primos(numero):
  factor=2
  while factor <=numero:
    if numero%factor==0:
      print(factor)
      numero=numero/factor
    else:
      factor+=1
numero=int(input())
print("descomposicion en factores primos:")
descomp_factores_primos(numero)