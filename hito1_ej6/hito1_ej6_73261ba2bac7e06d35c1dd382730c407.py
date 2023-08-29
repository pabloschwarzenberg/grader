#Ordenar tres números

numero1 = int(input("Ingresa el primer numero: "))
numero2 = int(input("Ingresa el segundo numero: "))
numero3 = int(input("Ingresa el tercer numero: "))

numero_minimo = min(numero1, numero2, numero3)
numero_maximo = max(numero1, numero2, numero3)

numero_medio = numero1 + numero2 + numero3 - numero_minimo - numero_maximo

print("Los numeros ordenados de menor a mayor son: ", numero_minimo, ",", numero_medio, ",", numero_maximo)