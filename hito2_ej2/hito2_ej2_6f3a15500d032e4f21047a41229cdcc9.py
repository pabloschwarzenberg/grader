def validar_secuencia(secuencia):
    # Convertir la secuencia a minúsculas y validar que solo contenga las letras adecuadas
    for letra in secuencia.lower():
        if letra not in "actg":
            return "secuencia incorrecta"
    return "secuencia correcta"

secuencia_adn = input("Ingrese la secuencia de ADN: ")
print(validar_secuencia(secuencia_adn))
