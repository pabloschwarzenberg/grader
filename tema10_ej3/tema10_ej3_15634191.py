def sopaletras(nombre_archivo,palabras):
    archivo=open(nombre_archivo,"r")
    filas=[]
    fil=archivo.readline()
    while fil != "":
        fil=fil.rstrip("\n")
        fil=fil.replace(" ","")
        filas.append(fil)
        fil=archivo.readline()
    columnas=[]
    for j in range(len(filas[1])):
        col=""
        for i in range(len(filas)):
                col+=filas[i][j]
        columnas.append(col)
    diagonales=[]
    for i in range(len(filas),1,-1):
        diag=""
        for j in range(len(filas)):
            diag+=filas[j+i-1][j]
            if j+1==len(columnas) or j+i==len(filas):
                break
        diagonales.append(diag)
    for i in range(len(columnas)):
        diag=""
        for j in range(len(columnas)):
            diag+=filas[j][j+i]
            if j+1==len(filas) or j+i+1==len(columnas):
                break
        diagonales.append(diag)
    archivo.close()
    dir=""
    sol=[]
    for palabra in palabras:
        palabra=palabra.upper()
        for i in filas:
            fil=filas.index(i)
            col=i.find(palabra)
            dir="derecha"
            if col != -1:
                break
        if col==-1:
            for i in columnas:
                col=columnas.index(i)
                fil=i.find(palabra)
                dir="abajo"
                if fil != -1:
                    break
        if fil == -1:
            for i in diagonales:
                if i.find(palabra) != -1:
                    dir="diagonal"
                    col=diagonales.index(i)-len(filas)+1+i.find(palabra)
                    if col<0:
                        col=0
                    if col==0:
                        fil=len(filas)-1-diagonales.index(i)+i.find(palabra)
                    else:
                        fil=i.find(palabra)
                    break
        loc=[fil,col]
        t=(palabra.lower(), loc, dir)
        sol.append(t)
    print(sol)
    return(sol)

if __name__=="__main__":
    sopaletras("sopa.txt",["casa","cra","aro"])
