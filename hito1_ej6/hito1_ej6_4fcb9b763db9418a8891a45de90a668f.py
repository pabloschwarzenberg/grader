#Ordenar tres números
numero1=int(input("ingrese el primer numero: "))
numero2=int(input("ingrese el segundo numero: "))
numero3=int(input("ingrese el tercer numero: "))
lista_numeros=[numero1, numero2, numero3]
lista_numeros.sort()
print("{}, {}, {}".format(lista_numeros[0],
lista_numeros[1],
lista_numeros[2]))