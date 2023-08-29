# completa el código de la función
def suma_divisores(a):
 n = int("Ingrese un numero: ")
 
  if n==1:
    return 1
  for i in range(2,n+1):
    if n%i == 0:
      return n+ sumaDivisores(n//i)
      
           