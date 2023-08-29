def sopaletras(nombre_archivo,palabras):
    Archivo = open(nombre_archivo,"r")

    Lineas = Archivo.readlines()
    Tablero = []

    for Linea in Lineas:
        Linea = Linea.strip("\n")
        Linea = Linea.split(" ")
        Tablero.append(Linea)

    for Palabra in palabras:
        for PosY in range(3):
            for PosX in range(len(Tablero[PosY])):
                if Tablero[PosY][PosX] == Palabra[0]:
                    # Derecha
                    if Tablero[PosY][PosX+1] == Palabra[1]:
                        encontrada = ""
                        for D in range(len(Palabra)):
                            encontrada = encontrada + Tablero[PosY][PosX+D]
                        if encontrada == Palabra:
                                print(Palabra,[PosY,PosX],"derecha")
                    # Abajo
                    if Tablero[PosY+1][PosX] == Palabra[1]:
                        encontrada = ""
                        for A in range(len(Palabra)):
                            encontrada = encontrada + Tablero[PosY+A][PosX]
                        if encontrada == Palabra:
                                print(Palabra,[PosY,PosX],"abajo")
                    # Diagonal
                    if Tablero[PosY+1][PosX+1] == Palabra[1]:
                        encontrada = ""
                        for C in range(len(Palabra)):
                            encontrada = encontrada + Tablero[PosY+C][PosX+C]
                        if encontrada == Palabra:
                                print(Palabra,[PosY,PosX],"diagonal")

if __name__=="__main__":
    print(sopaletras("sopa.txt",["cra"]))
    print(sopaletras("sopa.txt", ["aro"]))
    print(sopaletras("sopa.txt", ["casa"]))
    print(sopaletras("sopa.txt",["casa","cra","aro"]))

           