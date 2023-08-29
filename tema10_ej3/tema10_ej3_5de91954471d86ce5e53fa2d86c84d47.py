def sopaletras(nombre_archivo,palabras):
    archivo=open(nombre_archivo,"r")
    lista=[]
    for linea in archivo:
        fila=linea.lower().split()
        lista.append(fila)
    archivo.close()
    resultado=[]
    for pal in palabras:
        pal=pal.lower()
        diagonal=''
        for i in range(len(lista)):
            diagonal+=lista[i][i]
            columna=''
            for j in range(len(lista[0])):
                if j<len(lista):
                    columna+=lista[j][i]
            fila=''.join(lista[i])
            
            #print(columna)
            if pal in fila:
                resultado.append((pal,[i,fila.index(pal[0])],"derecha"))
            elif pal in columna:
                resultado.append((pal,[columna.index(pal[0]),i],"abajo"))
        if pal in diagonal:
            resultado.append((pal,[diagonal.index(pal[0]),diagonal.index(pal[0])],"diagonal"))
    #if len(resultado)==1:
    #    return resultado[0]
    #else:
    return resultado

if __name__=="__main__":
    #print(sopaletras("sopa.txt", ["casa"]))
    #print(sopaletras("sopa.txt",["cra"]))
    #print(sopaletras("sopa.txt", ["aro"]))
    print(sopaletras("sopa.txt",["casa","cra","aro"]))

           