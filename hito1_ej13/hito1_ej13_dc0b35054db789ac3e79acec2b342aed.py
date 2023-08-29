#Factores Primos
# Definir una función que encuentre el menor factor primo de un número
def menor_factor_primo(n):
    # Si el número es 1, no tiene factores primos
    if n == 1:
        return None
    # Si el número es par, el menor factor primo es 2
    if n % 2 == 0:
        return 2
    # Si el número es impar, se prueba con los impares desde 3 hasta la raíz cuadrada del número
    i = 3
    while i * i <= n:
        # Si el número es divisible por i, el menor factor primo es i
        if n % i == 0:
            return i
        # Si no, se incrementa i en 2 para probar con el siguiente impar
        i = i + 2
    # Si no se encontró ningún factor primo menor que la raíz cuadrada del número, el número es primo y su menor factor primo es él mismo
    return n

# Pedir al usuario que ingrese un número entero
n = int(input())

# Repetir el proceso hasta que el número sea 1
while n != 1:
    # Encontrar el menor factor primo del número
    factor = menor_factor_primo(n)
    # Imprimir el factor primo
    print(factor)
    # Dividir el número por el factor primo y asignar el resultado al número
    n = n // factor      