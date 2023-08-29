def seq(adn):
    adn.upper()
    adenina = "A" in adn
    timina  = "T" in adn
    guanina = "G" in adn
    citosina= "C" in adn
    if(adenina and timina and guanina and citosina):
        print("Secuencia correcta")
    else:
        print("Secuencia incorrecta")

adn = input("Ingrese su genoma: ")
print(seq(adn))
    
