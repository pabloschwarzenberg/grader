#Ordenar tres números
def encontrar_min_max_medio(num1, num2, num3):
    numeros = [num1, num2, num3]
    numeros.sort()
    minimo = numeros[0]
    medio = numeros[1]
    maximo = numeros[2]
    return minimo, medio, maximo
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))

minimo, medio, maximo = encontrar_min_max_medio(numero1, numero2, numero3)

print(minimo, "," ,medio, "," ,maximo)      