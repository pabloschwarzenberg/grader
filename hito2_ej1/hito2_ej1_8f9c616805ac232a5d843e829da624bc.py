def alinear_secuencias(adn1, adn2):
    alineacion = ""
    index_adn2 = 0
    
    for i in range(len(adn1)):
        if index_adn2 < len(adn2) and adn1[i] == adn2[index_adn2]:
            alineacion += adn2[index_adn2]
            index_adn2 += 1
        else:
            alineacion += "_"
    
    return alineacion


if __name__ == "__main__":
    adn1 = input("Ingrese la primera secuencia de ADN: ")
    adn2 = input("Ingrese la segunda secuencia de ADN: ")
    
    alineacion = alinear_secuencias(adn1, adn2)
    
    print(alineacion)



