      def imprimir_substrings_unicos(s, n):
    # Crear un diccionario para contar la frecuencia de los substrings
    substring_counts = {}

    # Obtener todos los substrings de longitud n
    for i in range(len(s) - n + 1):
        substring = s[i:i+n]
        if substring in substring_counts:
            substring_counts[substring] += 1
        else:
            substring_counts[substring] = 1

    # Imprimir los substrings únicos
    encontrados = False
    for substring, count in substring_counts.items():
        if count == 1:
            print(substring)
            encontrados = True

    # Imprimir mensaje si no se encontraron substrings únicos
    if not encontrados:
        print("ninguna")

# Solicitar al usuario que ingrese una secuencia y un número entero
s = input("Ingrese una secuencia: ")
n = int(input("Ingrese un número entero: "))

# Llamar a la función para imprimir los substrings únicos
imprimir_substrings_unicos(s, n)
