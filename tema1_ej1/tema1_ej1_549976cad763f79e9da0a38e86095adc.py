def suma_numeros_naturales(n):
  suma = (n * (n + 1)) // 2
  return suma

N = int(input("Ingresa un número entero positivo: "))
resultado = suma_numeros_naturales(N)
print("La suma de los", N, "primeros números naturales es:", resultado)
