#Ordenar tres números
numero_1 = int(input("inserte el primer numero: "))
numero_2 = int(input("inserte el segundo numero: "))
numero_3 = int(input("inserte el tercer numero: "))
numero_menor = min(numero_1, numero_2, numero_3)
numero_mayor = max(numero_1, numero_2, numero_3)
numero_medio = (numero_1 + numero_2 + numero_3) - numero_mayor - numero_menor
print("los numeros ordenados de menor a mayor seria: {}, {}, {} ".format(numero_menor, numero_medio, numero_mayor))     