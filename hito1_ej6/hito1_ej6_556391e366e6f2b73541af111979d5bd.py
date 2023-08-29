#Ordenar tres números
def ordenar_numeros(num1, num2, num3):
    numeros = [num1, num2, num3]
    numeros.sort()
    return numeros
    
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))

numeros_ordenados = ordenar_numeros(numero1, numero2, numero3)

resultado = ', '.join(str(numero) for numero in numeros_ordenados)

print("Los números ordenados de menor a mayor son:", resultado)      