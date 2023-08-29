def jerigonzo(string):
    i = 0
    matriz = list(string)
    print(matriz)
    j = len(matriz)
    print(j)
    
    while i < j:
        
        if matriz[i] == "a" :
            matriz[i] = "apa"
            i = i + 1
        elif matriz[i] == "e" :
            matriz[i] = "epe"
            i = i + 1
        elif matriz[i] == "i" :
            matriz[i] = "ipi"
            i = i + 1
        elif matriz[i] == "o" :
            matriz[i] = "opo"
            i = i + 1
        elif matriz[i] == "u" :
            matriz[i] = "upu"
            i = i + 1
        else:
            matriz[i] = matriz[i]
            i = i + 1
    matriz = matriz
    linea = ""
    for celda in matriz:
        linea = linea + str(celda)
    return linea

if __name__ == "__main__":
    pass
         
