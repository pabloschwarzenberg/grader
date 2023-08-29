def ocultar_letras(palabra,cantidad):
    import random
    posiciones = []
    
    for a in range(cantidad):
        b = random.randint(0,(len(palabra) - 1))
        while b in posiciones:
            b = random.randint(0,(len(palabra) - 1))
        else:
            posiciones.append(b)
            
    matriz = []
    for c in range(2):
        d = list(palabra)
        matriz.append(d)

    j = 0     
    while j < (len(posiciones)):
        k = posiciones[j]
        matriz[1][k] = "_"
        j = j + 1
    palabra_oculta = matriz[1]

    for fila in matriz:
        linea = ""
        for celda in fila:
          linea = linea + str(celda)
              
    return linea



def revisar_letra(palabra,palabra_secreta,letra):
    matriz = list(palabra_secreta)
    matriz_palabra = list(palabra)
    for l in range(len(palabra_secreta)):
        if matriz_palabra[l] == letra:
            matriz[l] = letra
            
    linea = ""

    for celda in matriz:
        linea = linea + str(celda)
        globals()["palabra_secreta"] = linea
        print(linea)
        print(palabra_secreta)
        print(globals()["palabra_secreta"])
    print("\n",linea)      
    return linea
            

