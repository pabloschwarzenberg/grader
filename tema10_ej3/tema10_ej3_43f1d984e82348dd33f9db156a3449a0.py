def sopaletras(nombre_archivo,palabras):
    archivo=open(nombre_archivo,"r")
    lineas=list(nombre_archivo)
    archivo.close()
    for j in palabras:
        i=0
        for k in lineas:
            o=list(k)
            while " " in o:
                o.remove(" ")
                k="".join(o)
            if j in k:
                return [(j,[i,k.find(j[0])],"derecha")]
            i+=1
    p=0
    l=[]
    for j in palabras:
        while p<len(lineas) and p<len(lineas[0]):
            q=0
            for k in lineas:
                l.append(k[p])
                l1="".join(l)
                if j in l1:
                    return [(j,[q,p],"abajo")]
                q+=1
            p+=1
    for j in palabras:
        a=0
        while (a+2)<len(j) and (a+2)<len(lineas[0]):
            if j[a]==lineas[a][a] and j[a+1]==lineas[a+1][a+1] and j[a+2]==lineas[a+2][a+2]:
                return [(j,[a,lineas[a].find(j[a])],"diagonal")]
            else:
                a+=1
                

if __name__=="__main__":
    print(sopaletras("sopa.txt",["cra"]))
    print(sopaletras("sopa.txt", ["aro"]))
    print(sopaletras("sopa.txt", ["casa"]))
    print(sopaletras("sopa.txt",["casa","cra","aro"]))

           