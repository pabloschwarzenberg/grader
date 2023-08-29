#Suma de los N primeros números
suma = 0

for i in range(1):
  numero = eval(input("ingrese un numero natural: "))
  suma = numero*(numero+1)/2

print(suma)