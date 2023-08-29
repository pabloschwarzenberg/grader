#Suma de los N primeros números
numero = int(input('Ingrese un número: '))
numero_final = 0
while numero_final < numero:
  numero_final = numero*(numero + 1)/2
print(int(numero_final))