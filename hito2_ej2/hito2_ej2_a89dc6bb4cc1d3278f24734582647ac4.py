def validar_secuencia_genoma(secuencia):
    # Convertir la secuencia a mayúsculas para evitar distinguir entre mayúsculas y minúsculas
    secuencia = secuencia.upper()

    # Verificar si la secuencia contiene únicamente las letras A, C, T y G
    for letra in secuencia:
        if letra not in ['A', 'C', 'T', 'G']:
            return "secuencia incorrecta"

    # Si no se encontraron letras no válidas, la secuencia es correcta
    return "secuencia correcta"

# Solicitar al usuario que ingrese la secuencia
secuencia = input("Ingrese la secuencia de ADN: ")

# Validar la secuencia e imprimir el resultado
resultado = validar_secuencia_genoma(secuencia)
print(resultado)
