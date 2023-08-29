def validar_secuencia(secuencia):
    # Convertir la secuencia a mayúsculas para no distinguir entre mayúsculas y minúsculas
    secuencia = secuencia.upper()

    # Verificar si la secuencia contiene solo las letras A, C, T y G
    for letra in secuencia:
        if letra not in ['A', 'C', 'T', 'G']:
            return False

    return True

# Solicitar al usuario que ingrese la secuencia
secuencia = input("Ingrese la secuencia del genoma: ")

# Validar la secuencia e imprimir el resultado
if validar_secuencia(secuencia):
    print("Secuencia correcta.")
else:
    print("Secuencia incorrecta.")
