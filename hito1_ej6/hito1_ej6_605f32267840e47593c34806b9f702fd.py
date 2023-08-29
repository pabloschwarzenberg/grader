#Ordenar tres números
numeroA = int(input("Ingrese un número: ")) 
numeroB = int(input("Ingrese otro número: ")) 
numeroC = int(input("Ingrese otro número: "))
numeros = [numeroA,numeroB,numeroC]
numerosOrdenados = sorted(numeros)
print(numerosOrdenados[0],",",numerosOrdenados[1],",",numerosOrdenados[2])