def sopaletras(nombre_archivo,palabras):
    Archivo = open(nombre_archivo,"r")

    Lineas = Archivo.readlines()
    Tablero = []
    Resultado = []
    for Linea in Lineas:
        Linea = Linea.lower()
        Linea = Linea.strip("\n")
        Linea = Linea.split(" ")
        Tablero.append(Linea)

    for Palabra in palabras:
        for PosY in range(len(Tablero)):
            for PosX in range(len(Tablero[PosY])):
                if Tablero[PosY][PosX] == Palabra[0]:
                    # Derecha
                    if PosX<=len(Tablero[PosY])-len(Palabra) and  Tablero[PosY][PosX+1] == Palabra[1]:
                        encontrada = ""
                        for D in range(len(Palabra)):
                            encontrada = encontrada + Tablero[PosY][PosX+D]
                        if encontrada == Palabra:
                                Resultado.append((Palabra,[PosY,PosX],"derecha"))
                    # Abajo
                    if PosY<=len(Tablero)-len(Palabra) and Tablero[PosY+1][PosX] == Palabra[1] :
                        encontrada = ""
                        for A in range(len(Palabra)):
                            encontrada = encontrada + Tablero[PosY+A][PosX]
                        if encontrada == Palabra:
                                Resultado.append((Palabra,[PosY,PosX],"abajo"))
                    # Diagonal
                    if PosY<=len(Tablero)-len(Palabra) and PosX<=len(Tablero[PosY])-len(Palabra) and Tablero[PosY+1][PosX+1] == Palabra[1]:
                        encontrada = ""
                        for C in range(len(Palabra)):
                            encontrada = encontrada + Tablero[PosY+C][PosX+C]
                        if encontrada == Palabra:
                                Resultado.append((Palabra,[PosY,PosX],"diagonal"))
    return Resultado

if __name__=="__main__":
    print(sopaletras("sopa.txt",["cra"]))
    print(sopaletras("sopa.txt", ["aro"]))
    print(sopaletras("sopa.txt", ["casa"]))
    print(sopaletras("sopa.txt",["casa","cra","aro"]))

           