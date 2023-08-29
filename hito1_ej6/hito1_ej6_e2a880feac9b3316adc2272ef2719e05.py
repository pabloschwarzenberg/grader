#Ordenar tres números
numero1 = int(input("ingresa un numero1: "))
numero2 = int(input("ingresa un numero2: "))
numero3 = int(input("ingresa un numero3: "))
numeros = numero1,numero2,numero3
print (numeros)
menor_a_mayor = sorted(numeros)
mayor_a_menor = sorted(numeros, reverse=True)
print (menor_a_mayor)
print (mayor_a_menor)