def ordenar_numeros(n1, n2, n3):
    numeros = [n1, n2, n3]
    numeros.sort()
    numeros_ordenados = ', '.join(str(num) for num in numeros)
    return numeros_ordenados
numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))
numero3 = int(input("Ingresa el tercer número: "))
#Agregar una variable para ordenar los numeros ingresados
numeros_ordenados = ordenar_numeros(numero1, numero2, numero3)
print("Números ordenados: ", numeros_ordenados)      