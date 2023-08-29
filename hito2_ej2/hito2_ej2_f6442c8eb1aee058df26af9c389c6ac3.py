def validar_secuencia_adn(secuencia):
    # Convertir la secuencia a mayúsculas
    secuencia = secuencia.upper()

    # Verificar si la secuencia contiene solo las letras A, C, T y G
    for letra in secuencia:
        if letra not in 'ACTG':
            return False

    return True

# Obtener la secuencia del usuario
secuencia_input = input("Ingresa la secuencia de ADN: ")

# Validar la secuencia y mostrar el resultado
if validar_secuencia_adn(secuencia_input):
    print("Secuencia correcta")
else:
    print("Secuencia incorrecta")