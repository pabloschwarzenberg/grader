#Factores Primos

n = int(input("descomponer: "))
def prime_factors(n):
  if n == 1: return []
  for div in range(2, n + 1):
      if n % div == 0: return [div] + prime_factors(n // div)
      
print("descomposicion", n)
  
