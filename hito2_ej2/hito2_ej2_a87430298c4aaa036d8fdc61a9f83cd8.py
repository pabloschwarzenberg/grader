def validar_secuencia(secuencia):
    # Convertir la secuencia a mayúsculas para comparar
    secuencia = secuencia.upper()

    # Verificar si la secuencia contiene solo las letras A, C, T y G
    for letra in secuencia:
        if letra not in ["A", "C", "T", "G"]:
            return False

    return True

# Obtener la secuencia de ADN del usuario
secuencia_adn = input("Ingrese la secuencia de ADN: ")

# Validar la secuencia y mostrar el resultado
if validar_secuencia(secuencia_adn):
    print("Secuencia correcta")
else:
    print("Secuencia incorrecta")
