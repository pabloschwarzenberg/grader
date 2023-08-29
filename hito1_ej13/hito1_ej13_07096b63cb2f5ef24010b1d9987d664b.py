#Factores Primos
numero = int(input("ingrese numero: "))
def prime_factors(numero):
  if numero == 1: return []
  for div in range(2,numero+1):
      if numero % div == 0: return [div] + prime_factors(numero // div)
print(prime_factors(numero))


