#Lista
numeros = []
#Ordenar tres números
a = int(input("Escriba el primer numero:  "))
b = int(input("Escriba el segundo numero:  "))
c = int(input("Escriba el tercer numero:  "))
#agregar numeros a la lista
numeros.append(a)
numeros.append(b)
numeros.append(c)
#ordenar lista de menor a mayor
numeros.sort()
print(str(numeros[0])+","+str(numeros[1])+","+str(numeros[2]))