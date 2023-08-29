#Suma de los N primeros números
n = int(input("Ingrese un numero entero: "))

suma = 0
i = 1

while i <= n:
  suma = suma + i
  i = i + 1
  
print("La suma de los pimeros", n, "numeros naturales es: ",suma)