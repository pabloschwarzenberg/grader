#Suma de los N primeros números
def suma_numeros_naturales(n):
  suma = (n * (n + 1)) // 2
  return suma 

n = int(input("ingrese el numero N:"))

resultado = suma_numeros_naturales(n)

print("la suma de los", n, "primeros numeros naturales es:", resultado)
