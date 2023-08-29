#Ordenar tres números
n1 = int(input("Ingrese número: "))
n2 = int(input("Ingrese número: "))
n3 = int(input("Ingrese número: ")) 

numeros = [n1, n2, n3]
numeros.sort()

resultado = ", ".join(str(n) for n in numeros)
print(resultado)
