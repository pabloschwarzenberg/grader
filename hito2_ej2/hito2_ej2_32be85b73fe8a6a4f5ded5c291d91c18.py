def validar_secuencia_genoma(secuencia):
    secuencia = secuencia.upper()  # Convertir a mayúsculas

    # Verificar si la secuencia contiene solo las letras A, C, T, G
    for letra in secuencia:
        if letra not in ['A', 'C', 'T', 'G']:
            return False

    return True

# Obtener la secuencia del genoma desde la entrada del usuario
secuencia_genoma = input("Ingrese la secuencia del genoma: ")

# Validar la secuencia del genoma
if validar_secuencia_genoma(secuencia_genoma):
    print("Secuencia correcta")
else:
    print("Secuencia incorrecta")
