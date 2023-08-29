def sopaletras(nombre_archivo, palabras):
 
    archivo = open(nombre_archivo, "r")

    txt = []
    for linea in archivo:
        txt += [linea.lower().strip().split(" ")]
    
    for linea in txt:
        if palabras[0] in "".join(linea):
            return [(palabras[0], [txt.index(linea), linea.index(palabras[0][0])], "derecha")]
    for i in range(len(txt[0])):
        ins = []
        for j in range(len(txt)):
            ins.append(txt[j][i])
            if palabras[0] in "".join(ins):
                return [(palabras[0], [j-len(txt)+1, i], "abajo")]
    diag = []
    for i in range(min(len(txt), len(txt[0]))):
        diag.append(txt[i][i])
        if palabras[0] in "".join(diag):
            return [(palabras[0], [i - len(palabras[0]) + 1, i - len(palabras[0]) + 1], "diagonal")]      
    archivo.close()

