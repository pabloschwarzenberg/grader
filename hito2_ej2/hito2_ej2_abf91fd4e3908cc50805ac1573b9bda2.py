def secuencia(adn):
    adn = str(adn.upper())
    Genoma = ["A", "C", "T", "G"]
    Gcantidad = 0
    
    for i in adn:

        if i in Genoma:
            Gcantidad += 1

        if Gcantidad == len(adn):

            return print("secuencia correcta")

        if i not in Genoma:
            
            return print("secuencia incorrecta")
            