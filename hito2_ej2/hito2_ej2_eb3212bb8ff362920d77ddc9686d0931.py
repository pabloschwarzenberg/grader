def validar_secuencia(secuencia):
    # Convertir la secuencia a letras mayúsculas
    secuencia = secuencia.upper()

    # Verificar si la secuencia contiene caracteres no válidos
    for letra in secuencia:
        if letra not in "ACTG":
            return False

    return True

# Solicitar la secuencia al usuario
secuencia = input("Introduce la secuencia de ADN: ")

# Validar la secuencia e imprimir el resultado
if validar_secuencia(secuencia):
    print("Secuencia correcta")
else:
    print("Secuencia incorrecta")     