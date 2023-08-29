# Definir una función que calcule la suma de los divisores de un número sin incluir al número
def suma_divisores(n):
    # Inicializar la suma con 0
    suma = 0
    # Recorrer los posibles divisores desde 1 hasta la raíz cuadrada del número
    i = 1
    while i * i <= n:
        # Si el número es divisible por i, se agrega i a la suma
        if n % i == 0:
            suma = suma + i
            # Si i no es 1 ni la raíz cuadrada del número, se agrega también el cociente de n e i a la suma
            if i != 1 and i * i != n:
                suma = suma + n // i
        # Incrementar i en 1 para probar con el siguiente divisor
        i = i + 1
    # Retornar la suma y si el número es primo o no (si la suma es 1, el número es primo)
    return suma, suma == 1

# Probar la función con algunos ejemplos
if __name__ == "__main__":
    print(suma_divisores(6)) # Debe imprimir (6, False)
    print(suma_divisores(13)) # Debe imprimir (0, False)
    print(suma_divisores(28)) # Debe imprimir (28, False)

           