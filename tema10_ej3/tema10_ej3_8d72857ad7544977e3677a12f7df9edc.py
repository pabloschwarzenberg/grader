def sopaletras(nombre_archivo,palabras):
    tablero=[]
    archivo=open(nombre_archivo,"r")
    for lineas in archivo:
        l=lineas.split()
        tablero.append(l)
    archivo.close()
    resultado=[]
    for palabra in palabras:
        palabra1=palabra
        palabra=palabra.upper()
        for f in range(len(tablero)):
            for c in range(len(tablero[f])):

                if palabra[0]==tablero[f][c]:
                    horizontal=""
                    for c1 in range(c,len(tablero[f])):
                        horizontal=horizontal+tablero[f][c1]

                    vertical=""
                    for f1 in range(f,len(tablero)):
                        vertical=vertical+tablero[f1][c]    

                    diagonal=""
                    for f1 in range(f,len(tablero)):
                        for c1 in range(c,len(tablero[0])):
                            if f1 ==c1:
                                diagonal=diagonal+tablero[f1][c1]  

                    if palabra==horizontal:

                        pos=[f,c]
                        direccion="derecha"

                    elif palabra==vertical:

                        pos=[f,c]
                        direccion="abajo"

                    elif palabra==diagonal:

                        pos=[f,c]
                        direccion="diagonal"
                    
                    agregar=(palabra1,pos,direccion)
                    if not agregar in resultado:
                        resultado.append(agregar)
    return resultado

           