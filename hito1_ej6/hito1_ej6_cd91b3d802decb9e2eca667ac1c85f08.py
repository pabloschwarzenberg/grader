#Ordenar tres números
numero_1 = input ("Ingresar número: ")
numero_2 = input ("Ingresar número: ")
numero_3 = input ("Ingresar número: ")
numeros = [int (numero_1), int (numero_2), int(numero_3)]
print("Los números son: ", numeros)
print("")
numeros.sort()
print("Los números en orden de menor a mayor son: ", numeros)