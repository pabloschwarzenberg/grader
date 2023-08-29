#Suma de los N primeros números
def suma_numeros_naturales(n):
  return (n*(n+1))/2
 
n = int(input("Ingresa n: "))
print(suma_numeros_naturales(n))