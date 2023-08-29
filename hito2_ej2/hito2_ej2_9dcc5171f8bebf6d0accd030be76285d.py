def validar_secuencia_genoma(secuencia):
    # Convertir la secuencia a minúsculas para ignorar las mayúsculas
    secuencia = secuencia.lower()

    # Validar si la secuencia contiene solo las letras A, C, T y G
    for letra in secuencia:
        if letra not in ['a', 'c', 't', 'g']:
            return False

    return True


# Obtener la secuencia del genoma desde el usuario
secuencia_genoma = input("Ingrese la secuencia del genoma: ")

# Validar la secuencia del genoma
if validar_secuencia_genoma(secuencia_genoma):
    print("Secuencia correcta")
else:
    print("Secuencia incorrecta")
