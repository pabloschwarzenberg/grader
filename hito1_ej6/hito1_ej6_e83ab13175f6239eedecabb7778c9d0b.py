#Ordenar tres números
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))

numeros = [numero1, numero2, numero3]

numeros.sort(reverse=False)

print("Los números ordenados de menor a mayor son:", numeros[0], ",", numeros[1], ",", numeros[2])