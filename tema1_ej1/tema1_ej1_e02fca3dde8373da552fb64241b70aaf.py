def suma_numeros_naturales(N):
    # Calcula la suma de los primeros N números naturales
    suma = N * (N + 1) // 2

    # Imprime el resultado
    print(f'La suma de los primeros {N} números naturales es: {suma}')

# Solicita un número al usuario
N = int(input('Introduce un número: '))

suma_numeros_naturales(N)