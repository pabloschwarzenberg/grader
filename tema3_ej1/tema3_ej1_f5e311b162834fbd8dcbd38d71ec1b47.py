# completa el código de la función
n = int(input("ingrese el numero"))
def suma_divisores(n):
  divisores = [1]
  for i in range(2,n+1):
    if n%i==0:
      divisores.append(i)
  return sum(divisores)
resultado = suma_divisores(n)
print(resultado)
           