#Ordenar tres números
print("Programa para ordenar numeros enteros de menor a mayor")

numero1 = int(input("Ingrese un numero entero: "))
numero2 = int(input("Ingrese un numero entero: "))
numero3 = int(input("Ingrese un numero entero: "))

lista=[numero1, numero2, numero3]
listaOrdenada=sorted(lista)


print(listaOrdenada[0],",",listaOrdenada[1],",",listaOrdenada[2])


