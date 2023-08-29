#Ordenar tres números

numeros = []

for i in range (3):

    num=int(input("ingresa un número entero: "))

    numeros.append(num)

   

numeros.sort()

ordenados=",".join(str(num)for num in numeros)

print("Los números ordenados de menor a mayor son:", ordenados) 
      