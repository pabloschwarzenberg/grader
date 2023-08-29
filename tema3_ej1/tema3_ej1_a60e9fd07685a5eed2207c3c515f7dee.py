# completa el código de la función
def suma_divisores(n):
  divisores = [i for i in range(1, n+1) if n%i ==0]
  
  return sum(divisores)
resultado = suma_divisores(n)
n= int(intput("ingrese numero")

 print(resultado)