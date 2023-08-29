#Ordenar tres números

#Entrada de datos
n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))
n3 = int(input("Ingrese el tercer numero: "))

#Comparacion
if n1 <= n2 and n1 <= n3:
    n_menor = n1
    if n2 <= n3:
        n_medio = n2
        n_mayor = n3
    else:
        n_medio = n3
        n_mayor = n2
elif n2 <= n1 and n2 <= n3:
    n_menor = n2
    if n1 <= n3:
        n_medio = n1
        n_mayor = n3
    else:
        n_medio = n3
        n_mayor = n1
else:
    n_menor = n3
    if n1 <= n2:
        n_medio = n1
        n_mayor = n2
    else:
        n_medio = n2
        n_mayor = n1
#salida
print(str(n_menor) + "," + str(n_medio) + "," + str(n_mayor))