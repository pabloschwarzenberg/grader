#Suma de los N primeros números
def suma_naturales(n):
  suma= (n*(n+1))//2
  return suma
  
N = int(input("ingrese el numero natural:"))
suma_total = suma_naturales(N)
print("la suma de los primeros", N,"numeros naturales es:", suma_total)