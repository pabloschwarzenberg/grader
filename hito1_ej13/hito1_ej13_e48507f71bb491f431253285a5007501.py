#Factores Primos
def primo(n):
  if n == 1: 
    return []
  for div in range(2, n + 1):
      if n % div == 0: 
        return [div] + primo(n // div) 
numero=int(input("Ingrese numero: "))
print(primo(numero))
