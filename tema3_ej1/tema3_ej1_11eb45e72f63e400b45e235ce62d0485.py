# completa el código de la función
def suma_divisores(n):
  divisores=[]
  for i in range(1,n):
   if n%i==0:
     divisores.append(i)
  return sum(divisores)
def numero_primo(n):
  if n<2:
    return False
  for j in range(2,n):
    if n%j==0:
     return False
    return True