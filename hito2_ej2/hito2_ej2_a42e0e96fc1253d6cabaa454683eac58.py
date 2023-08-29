def validador_secuencia(adn):
    adn=adn.upper()
    if "B" not in adn and "D" not in adn and "E" not in adn and "F" not in adn and "H" not in adn and "I" not in adn and "J" not in adn and "K" not in adn and "L" not in adn and "M" not in adn and "N" not in adn and "O" not in adn and "P" not in adn and "Q" not in adn and "R" not in adn and "S" not in adn and "U" not in adn and "V" not in adn and "W" not in adn and "X" not in adn and "Y" not in adn and "Z" not in adn:
        validador="secuencia correcta"
    else:
        validador="secuencia incorrecta"
    return validador

adn=input()
print(validador_secuencia(adn))
