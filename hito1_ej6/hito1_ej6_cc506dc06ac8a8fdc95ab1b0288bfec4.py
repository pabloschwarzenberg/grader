#Ordenar tres números
def ordenar_numeros(n1, n2, n3):
    numeros = [n1, n2, n3]
    numeros.sort()
    numeros_ordenados = ", ".join(map(str, numeros))
    return numeros_ordenados

# Solicitar números al usuario
numero1 = int(input("Digite el primer número: "))
numero2 = int(input("Digite el segundo número: "))
numero3 = int(input("Digite el tercer número: "))

# Ordenar y mostrar los números
numeros_ordenados = ordenar_numeros(numero1, numero2, numero3)
print("Números ordenados:", numeros_ordenados)      