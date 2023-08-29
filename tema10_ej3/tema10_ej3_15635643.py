__author__ = 'Martín Cepeda'
def sopaletras(nombre_archivo,lista_palabras):
    palabras=[]
    for i in lista_palabras:
        palabras.append(i.upper())
    archivo=open(nombre_archivo,"r")
    filas=[]
    columnas=[]
    diagonales=[]
    for linea in archivo:
        letras=linea.strip("\n")
        g=letras.split(" ")
        letras="".join(g)
        filas.append(letras)
    archivo.close()
    for i in range(len(filas[0])):
        pal_col=""
        for line in filas:
            pal_col+=line[i]
        columnas.append(pal_col)
    a=0
    pal_diag=""
    for i in range(len(filas)):
        pal_diag+=filas[i][a]
        a+=1
    diagonales.append(pal_diag)
    a=0
    pal_diag=""
    for i in range(len(filas)):
        pal_diag+=filas[i][a+1]
        a+=1
    diagonales.append(pal_diag)
    resultado=[]
    for palabra in palabras:
        word=lista_palabras[palabras.index(palabra)]
        for linea in filas:
            if palabra in linea:
                resultado.append((word,[filas.index(linea),linea.index(palabra)],"derecha"))
        for col in columnas:
            if palabra in col:
                resultado.append((word,[col.index(palabra),columnas.index(col)],"abajo"))
        for diag in diagonales:
            if palabra in diag:
                resultado.append((word,[diag.index(palabra),diagonales.index(diag)],"diagonal"))
    return resultado

if __name__=="__main__":
    pass

           