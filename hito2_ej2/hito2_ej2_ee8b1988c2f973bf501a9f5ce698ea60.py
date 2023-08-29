def es_secuencia_genoma(secuencia):
    # Verificar que la secuencia solo contenga las letras A, C, T, G
    for letra in secuencia:
        if letra not in 'ACTG':
            return False
    return True

# Obtener la secuencia del usuario
secuencia_input = input("Ingrese la secuencia de ADN: ")

# Convertir la secuencia a mayúsculas
secuencia = secuencia_input.upper()

# Validar la secuencia del genoma
if es_secuencia_genoma(secuencia):
    print("Secuencia correcta")
else:
    print("Secuencia incorrecta")
