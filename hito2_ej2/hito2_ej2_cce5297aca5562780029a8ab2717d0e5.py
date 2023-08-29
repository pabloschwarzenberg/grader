def validar_secuencia(secuencia):
    secuencia = secuencia.upper()  # Convertir la secuencia a mayúsculas

    for letra in secuencia:
        if letra not in {'A', 'C', 'T', 'G'}:
            return False

    return True

# Solicitar la secuencia al usuario
secuencia = input("Ingrese la secuencia de ADN: ")

# Validar la secuencia
if validar_secuencia(secuencia):
    print("Secuencia correcta")
else:
    print("Secuencia incorrecta")
