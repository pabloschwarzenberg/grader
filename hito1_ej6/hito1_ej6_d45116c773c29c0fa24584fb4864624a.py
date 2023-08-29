#Ordenar tres números
numero1 = int(input("Ingrese un numero entero:  "))
numero2 = int(input("Ingrese un numero entero: "))
numero3 = int(input("Ingrese un numero entero: "))
# Ordenar los números de menor a mayor
if numero1 <= numero2 <= numero3:
  numeros_ordenados = numero1, numero2, numero3
elif numero1 <= numero3 <= numero2:
  numeros_ordenados = numero1, numero3, numero2
elif numero2 <= numero1 <= numero3:
  numeros_ordenados = numero2, numero1, numero3
elif numero2 <= numero3 <= numero1:
  numeros_ordenados = numero2, numero3, numero1
elif numero3 <= numero1 <= numero2:
  numeros_ordenados = numero3, numero1, numero2
else:
  numeros_ordenados = numero3, numero2, numero1

print("Números de mayor a menor", numeros_ordenados)
