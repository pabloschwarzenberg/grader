def validar_secuencia(secuencia):
    # Convertir la secuencia a minúsculas
    secuencia = secuencia.lower()

    # Verificar si la secuencia contiene solo las letras A, C, T y G
    for letra in secuencia:
        if letra not in ['a', 'c', 't', 'g']:
            return False

    return True


# Obtener la secuencia del usuario
secuencia = input("Ingrese la secuencia de ADN: ")

# Validar la secuencia
if validar_secuencia(secuencia):
    print("Secuencia correcta")
else:
    print("Secuencia incorrecta")

