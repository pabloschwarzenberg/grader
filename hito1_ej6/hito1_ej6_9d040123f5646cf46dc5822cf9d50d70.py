#Ordenar tres números
n1 = int(input('Ingrese el primer numero: '))
n2 = int(input('Ingrese el segundo numero: '))
n3 = int(input('Ingrese el tercer numero: '))
Lista = [n1, n2, n3]
Lista.sort()
print(str(Lista[0]) + ',' + str(Lista[1]) + ',' + str(Lista[2]))