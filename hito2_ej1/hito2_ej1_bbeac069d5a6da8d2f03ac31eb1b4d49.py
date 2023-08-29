def alinear(adn1, adn2):
    adn1 = list(adn1.upper())
    adn2 = list(adn2.upper())
    
    i = 0
    while i < len(adn1):
        if adn1[i] == adn2[i]:
            i += 1
        else:
            adn2.insert(i,"_")
            i += 1
    return "".join(adn2)