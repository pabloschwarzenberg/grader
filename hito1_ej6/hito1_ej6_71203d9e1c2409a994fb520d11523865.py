#Ordenar tres números
a = int(input("Ingrese un número "))
b = int(input("Ingrese otro número "))
c = int(input("Ingrese otro número "))
numeros = []
numeros.append(a)
numeros.append(b)
numeros.append(c)
numeros.sort()
for numero in numeros:
    print(numero,)
