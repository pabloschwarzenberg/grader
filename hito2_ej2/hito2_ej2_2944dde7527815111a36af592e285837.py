def cadena(adn):
    
    if adn == "ACGT" or "acgt" :
        return ("secuencia correcta")
        
    else:
        return ("secuencia incorrecta")




if __name__ == "__main__":
    adn=str(input("escriba la secuencia:"))
    print(cadena(adn))
                 