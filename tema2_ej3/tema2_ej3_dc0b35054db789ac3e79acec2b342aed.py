# Definir una función que reciba un número y retorne True si es un número perfecto, y False en caso de no serlo
def numero_perfecto(n):
    # Inicializar la suma de los divisores con 0
    suma = 0
    # Recorrer los posibles divisores desde 1 hasta la mitad del número
    for i in range(1, n // 2 + 1):
        # Si el número es divisible por i, se agrega i a la suma
        if n % i == 0:
            suma = suma + i
    # Retornar si la suma es igual al número o no
    return suma == n

# Probar la función con algunos ejemplos
if __name__ == "__main__":
    print(numero_perfecto(6)) # Debe imprimir True
    print(numero_perfecto(28)) # Debe imprimir True
    print(numero_perfecto(15)) # Debe imprimir False

           