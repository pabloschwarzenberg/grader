      def alinear_secuencias(adn1, adn2):
    if len(adn1) >= len(adn2):
        alineado = adn2 + '_' * (len(adn1) - len(adn2))
    else:
        alineado = adn2[:len(adn1)]

    return alineado

# Solicitar al usuario que ingrese las secuencias de ADN
adn1 = input("Ingrese la primera secuencia de ADN: ")
adn2 = input("Ingrese la segunda secuencia de ADN: ")

# Obtener la secuencia alineada
secuencia_alineada = alinear_secuencias(adn1, adn2)

# Imprimir la secuencia alineada
print(secuencia_alineada)
