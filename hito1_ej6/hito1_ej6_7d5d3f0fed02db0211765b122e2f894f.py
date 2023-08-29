#Ordenar tres números
nro_1 = eval(input("Ingrese el primer número "))
nro_2 = eval(input("Ingrese el segundo número "))
nro_3 = eval(input("Ingrese el tercer número "))
lista = nro_1, nro_2, nro_3
lista_ordenada = sorted(lista)
print (*(lista_ordenada), sep=", ")