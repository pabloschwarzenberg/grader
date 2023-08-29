#Ordenar tres números
numero_1 = int(input("Ingresa un número: "))
numero_2 = int(input("Ingresa otro número: "))
numero_3 = int(input("Ingresa un último número: "))

sumatoria = numero_1 + numero_2 + numero_3
mayor = max(numero_1, numero_2, numero_3)
menor = min(numero_1,numero_2, numero_3)
medio = sumatoria - mayor - menor

print(str(menor) + ", " + str(medio) + ", " + str(mayor))