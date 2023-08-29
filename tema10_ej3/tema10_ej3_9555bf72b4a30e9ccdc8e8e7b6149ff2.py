def sopaletras(nombre_archivo,palabras):
    palabras=list(map(lambda x:x.upper(),palabras))
    lista=[]
    archivo=open(nombre_archivo,"r")
    filas=archivo.readlines()
    for fila in filas:
        filas[filas.index(fila)]=fila.replace(" ","").replace("\n","")
    columnas=[""]*len(filas[0])
    diag=[""]*(len(filas)+len(filas[0])-1)
    i=0
    while i<len(filas[0]):
        j=0
        d=""
        while True:
            try:
                d+=filas[j+i][j]
                j+=1
            except IndexError:
                diag[len(filas)-1-i]=d
                i+=1
                break
    i=1
    while i<=len(filas):
        j=0
        d=""
        while True:
            try:
                d+=filas[j][j+i]
                j+=1
            except IndexError:
                diag[len(filas)+i-1]=d
                i+=1
                break
    for i in range(len(filas)):
        for palabra in palabras:
            a=filas[i].find(palabra)
            if a>=0:
                lista.append((palabra.lower(),[i,a],"derecha"))
        for j in range(len(filas[0])):
            columnas[j]+=filas[i][j]
    for i in range(len(columnas)):
        for palabra in palabras:
            a=columnas[i].find(palabra)
            if a>=0:
                lista.append((palabra.lower(),[a,i],"abajo"))
    for diagonal in diag:
        for palabra in palabras:
            a=diagonal.find(palabra)
            if len(filas)-1>=a>=0:
                f=len(filas)-1-diag.index(diagonal)+a
                c=a
            elif len(filas)<=a<len(diag):
                f=a
                c=diag.index(diagonal)-len(fila[0])-1+a
            else:
                continue
            lista.append((palabra.lower(),[f,c],"diagonal"))
    archivo.close()
    return lista