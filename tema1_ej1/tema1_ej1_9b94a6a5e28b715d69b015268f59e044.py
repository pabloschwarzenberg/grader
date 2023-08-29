#Suma de los N primeros números
print("Ingrese un numero")
N = int(input())
suma = 0
for contador in range(1,N + 1):
  suma = suma + contador
print(suma)      