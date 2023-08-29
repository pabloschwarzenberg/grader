#Ordenar tres números
     #Ordenar tres números
numeros = []
for i in range(3):
    numeros.append(int(input("Ingresa un número entero: ")))
numeros.sort()
print("Los números ordenados son:", end=" ")
for numero in numeros:
    print(numero, end=", ")