def sopaletras(nombre_archivo,palabras):
    S = []
    archivo=open(nombre_archivo,"r")
    for linea in archivo:
        if linea[-1] == "\n":
            linea = linea[:-1]
        linea = linea.replace(" ","")
        fila = list(linea)
        S.append(fila)
    archivo.close()
    M, N = len(S), len(S[0])
    SAL = []
    x=0
    while x <len(palabras):
        pal = palabras[x]
        encontrado = False
        i=0
        while i<M and not encontrado:
            j=0
            while j<N and not encontrado:
                pi = i
                pj = j
                k=0
                while k<len(pal) and i<M and j<N:
                    if S[i][j] != pal[k]:
                        break
                    k += 1
                    j += 1
                if k == len(pal): #encontro palabra
                    salida = (pal, [pi,pj], "derecha")
                    SAL.append(salida)
                    encontrado = True
                j = j+1
            i = i+1
        if encontrado:
            x+=1
            continue
        j=0
        while j<N and not encontrado:
            i=0
            while i<M and not encontrado:
                pi = i
                pj = j
                k=0
                while k<len(pal) and j<N and i<M:
                    if S[i][j] != pal[k]:
                        break
                    k += 1
                    i += 1
                if k == len(pal): #encontro palabra
                    salida = (pal, [pi,pj], "abajo")
                    SAL.append(salida)
                    encontrado = True
                i += 1
            j += 1
        if encontrado:
            x+=1
            continue
        i=0
        while i<min(M,N):
            pi = i
            pj = i
            k=0
            while k<len(pal) and i<min(M,N):
                if S[i][i] != pal[k]:
                    break
                k += 1
                i += 1
            if k == len(pal): #encontro palabra
                salida = (pal, [pi,pj], "diagonal")
                SAL.append(salida)
                encontrado = True
            i = i+1        
        x=x+1
    SAL = tuple(SAL)
    return SAL  

#def sopaletras(nombre_archivo,palabras):
#    archivo=open(nombre_archivo,"r")
#    archivo.close()
#    return [(palabras[0],[0,0],"diagonal")]

if __name__=="__main__":
    print(sopaletras("sopa.txt",["cra"]))
    print(sopaletras("sopa.txt", ["aro"]))
    print(sopaletras("sopa.txt", ["casa"]))
    print(sopaletras("sopa.txt",["casa","cra","aro"]))

           