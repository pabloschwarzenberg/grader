def alinear_secuencias(adn1, adn2):
    alineacion = ''
    i = 0
    
    for c in adn2:
        if c == adn1[i]:
            alineacion += c
            i += 1
        else:
            alineacion += '_'
    
    return alineacion

if __name__ == "__main__":
    adn1 = input("Ingrese la primera secuencia de ADN: ")
    adn2 = input("Ingrese la segunda secuencia de ADN: ")
    
    resultado = alinear_secuencias(adn1, adn2)
    
    print(resultado)
      