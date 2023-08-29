#Ordenar tres números

#Recibir numeros como enteros:
lista = []

lista.append(int(input("Ingresa el primer numero: ")))
lista.append(int(input("Ingresa el segundo numero: ")))
lista.append(int(input("Ingresa el tercer numero: ")))

lista.sort()

print(str(lista[0]) + ", " + str(lista[1]) + ", " + str(lista[2]))     

