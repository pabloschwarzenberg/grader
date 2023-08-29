def verif_adn(adn):
    corr = "Secuencia correcta"
    inco = "Secuencia incorrecta"
    adn = adn.upper()
    for letra in adn:
        if letra not in ["A", "C", "T", "G"]:
            return inco
    return corr

adn = input("Ingrese la secuencia de ADN: ")
print(verif_adn(adn))
