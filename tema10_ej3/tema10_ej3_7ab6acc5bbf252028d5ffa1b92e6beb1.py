def sopaletras(nombre_archivo,palabras):
    resultado=[]
    for palabra in palabras:
        r=sopaletras2(nombre_archivo,palabra)
        resultado.append(r)
    return resultado

def sopaletras2(nombre_archivo,palabras):
    archivo=open(nombre_archivo,"r")
    palabras="".join(palabras).upper()
    a=""
    for i in archivo:
        c=""
        for b in str(i):
            if b==" ":
                continue
            else:
                c=c+b
        a=a+"{0}".format(c)
    lista=a.split("\n")
    for j in range(len(lista)):
        if palabras in lista[j]:
            a=palabras.lower()
            b= [j,lista[j].index(palabras)]
            c="derecha"
            return ("{0}".format(a), b, "{0}".format(c))
        elif palabras in lista[j][::-1]:
            a = palabras.lower()
            d=list(palabras[::-1])
            b=[j,lista[j].index(d[0])]
            c = "izquierda"
            return ("{0}".format(a), b, "{0}".format(c))
    for i in range(len(lista)):
        if palabras in (lista[0][i]+lista[1][i]+lista[2][i]):
            k = [lista[0][i] + lista[1][i] + lista[2][i]]
            a=palabras.lower()
            b=[k.index(palabras),i]
            c="abajo"
            return ("{0}".format(a), b, "{0}".format(c))
        #elif palabras[i] in (lista[2][i]+lista[1][i]+lista[0][i]):
            #k = [lista[2][i]+lista[1][i]+lista[0][i]]
            #a = palabras.lower()
            #b = [len(lista)-1-k.index(palabras), i]
            #c = "arriba"
            #return ("{0}".format(a), b, "{0}".format(c))
    if palabras in (lista[0][0]+lista[1][1]+lista[2][2]):
        a= palabras.lower()
        b=[0,0]
        c="diagonal"
        return ("{0}".format(a), b, "{0}".format(c))
    if palabras in (lista[0][1] + lista[1][2] + lista[2][3]):
        a = palabras.lower()
        b = [0, 1]
        c = "diagonal"
        return ("{0}".format(a), b, "{0}".format(c))
    if palabras in (lista[0][2] + lista[1][1] + lista[2][0]):
        a = palabras.lower()
        b = [0, 2]
        c = "diagonal"
        return ("{0}".format(a), b, "{0}".format(c))
    if palabras in (lista[0][3] + lista[1][2] + lista[2][1]):
        a = palabras.lower()
        b = [0, 3]
        c = "diagonal"
        return ("{0}".format(a), b, "{0}".format(c))

    archivo.close()

if __name__=="__main__":
    print(sopaletras("sopa.txt",["cra"]))
    print(sopaletras("sopa.txt", ["aro"]))
    print(sopaletras("sopa.txt", ["casa"]))
    print(sopaletras("sopa.txt",["casa","cra","aro"]))

           