# Crea una función que calcule la suma de los divisores de un número sin incluir al número, llamada suma_divisores. Junto con la suma de los divisores haz que la función retorne si el número es primo o no, basándose en que si la suma de sus divisores es 1, el número es primo.
def suma_divisores(n):
  divisores=[]
  for i in range(1,n+2):
   if n%i==0:
     divisores.append(i)
  return sum(divisores)
def numero_primo(n):
  if n<2:
    return False
  for j in range(2,n+2):
    if n%j==0:
     return False
    return True
if __name__ == "__main__":
  n=int(input("inserte numero:" ))
  rsuma=suma_divisores(n)
  rprimos=numero_primo(n)
  print (rsuma,rprimos)
    