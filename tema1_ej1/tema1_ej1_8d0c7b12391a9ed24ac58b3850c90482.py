#Suma de los N primeros números
def suma_naturales(n):
  suma= n*(n + 1)/2
  return suma
n = int(input('ingrese unos de los primeros numeros naturales: '))
sum = suma_naturales(n)
print(sum)