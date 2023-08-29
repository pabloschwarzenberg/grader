def horizontal(tablero,palabra):
    fila=0
    f=len(tablero)
    c=len(tablero[0])
    l=len(palabra)
    while fila<f:
        k=0
        columna=0
        while columna<c and k<l:
            if tablero[fila][columna]!=palabra[k].upper():
                break
            else:
                columna+=1
                k+=1
        if k==l:
            return (palabra,[fila,0],"derecha")
        fila+=1
    return None

def vertical(tablero,palabra):
    columna=0
    f=len(tablero)
    c=len(tablero[0])
    l=len(palabra)
    while columna<c:
        k=0
        fila=0
        while fila<f and k<l:
            if tablero[fila][columna]!=palabra[k].upper():
                break
            else:
                fila+=1
                k+=1
        if k==l:
            return (palabra,[0,columna],"abajo")
        columna+=1
    return None

def diagonal(tablero,palabra):
    inicio=0
    f=len(tablero)
    c=len(tablero[0])
    l=len(palabra)
    while inicio<c:
        k=0
        fila=0
        columna=inicio
        while fila<f and columna<c and k<l:
            if tablero[fila][columna]!=palabra[k].upper():
                break
            else:
                fila+=1
                columna+=1
                k+=1
        if k==l:
            return (palabra,[0,inicio],"diagonal")
        inicio+=1
    return None

def sopaletras(archivo,palabras):
    tablero=[]
    ubicaciones=[]
    archivo=open(archivo,"r")
    for linea in archivo:
        celdas=linea.strip().split(" ")
        tablero.append(celdas)
    d=len(tablero)
    for palabra in palabras:
        p=horizontal(tablero,palabra)
        if p is not None:
            ubicaciones.append(p)
            continue
        p=vertical(tablero,palabra)
        if p is not None:
            ubicaciones.append(p)
            continue
        p=diagonal(tablero,palabra)
        if p is not None:
            ubicaciones.append(p)
            continue
    return ubicaciones

if __name__ == "__main__":
    print(sopaletras("sopa.txt",["casa","cra","aro"]))