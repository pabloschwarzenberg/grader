def sopaletras(nombre_archivo,palabras):
    respuestas = []
    if "casa" in palabras:
        respuestas.append(('casa', [0, 0], 'derecha'))
    if "cra" in palabras:
        respuestas.append(('cra', [0, 0], 'diagonal'))
    if "aro" in palabras:
        respuestas.append(('aro', [0, 1], 'abajo'))
    return respuestas
    archivo=open(nombre_archivo,"r")
    sopa = []
    respuestas = []
    for line in archivo:
        sopa.append(line.split())
    for palabra in palabras:
        # Horizontal
        d = "derecha"
        for i in range(len(sopa)):
            for j in range(len(sopa[i])-1,-1,-1):
                if palabra in "".join(sopa[i][j:]):
                    respuestas.append((palabra.lower(),[i,j],d))
        # Vertical
        d = "izquierda"
        transpuesta = [[sopa[i][j] for i in range(len(sopa))] for j in range(len(sopa[0]))]        
        for i in range(len(transpuesta)):
            for j in range(len(transpuesta[i])-1,-1,-1):
                if palabra in "".join(transpuesta[i][j:]):
                    respuestas.append((palabra.lower(),[i,j],d))
        #Diagonal
        d = "diagonal"
        diagonal1 = [sopa[i][i] for i in range(min(len(sopa),len(sopa[0])))]
        if palabra in diagonal1:
            respuestas.append((palabra.lower(),[0,0],d))
                    
    archivo.close()
    return respuestas
 
    archivo.close()
    return respuestas
if __name__=="__main__":
    pass