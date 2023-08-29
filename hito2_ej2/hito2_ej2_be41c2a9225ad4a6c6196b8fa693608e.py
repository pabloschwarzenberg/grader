def validar_secuencia(secuencia):
    # Convertir la secuencia a mayúsculas para no distinguir entre mayúsculas y minúsculas
    secuencia = secuencia.upper()

    # Verificar si la secuencia contiene solo las letras A, C, T y G
    for letra in secuencia:
        if letra not in ['A', 'C', 'T', 'G']:
            return False

    return True

# Pedir al usuario que ingrese una secuencia de ADN
secuencia_adn = input()

# Validar la secuencia ingresada
if validar_secuencia(secuencia_adn):
    print("secuencia correcta")
else:
    print("secuencia incorrecta")
      