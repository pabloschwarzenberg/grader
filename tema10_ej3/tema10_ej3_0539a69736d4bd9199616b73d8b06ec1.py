def sopaletras(nombre_archivo,palabras):
    archivo=open(nombre_archivo,"r")
    leer=archivo.readlines()
    archivo.close()
    archivo=open(nombre_archivo,"r")
    lista=[]
    for i in range(len(leer)):
        b=archivo.readline()
        c=b.split("\n")
        for n in range(len(c)):
            if c[n] == "":
                c.remove("")
        for n in c:
            e=str(n)
            e=e.split(" ")
            lista.append(e)
    temporal1=[]
    for i in palabras:
        i=i.upper()
        temporal1.append(i)
    lar1=len(lista)
    lar2=len(lista[0])
    coordenadas=[]
    for z in range(len(temporal1)):
        for y in range(lar1):
            for x in range(lar2):
                if lista[y][x] == temporal1[z][0]:
                    coordenadas.append([y,x])
    lar3=[]
    lar4=[]
    lar5=[]
    for i in range(len(coordenadas)):
        lar3.append(lar2-coordenadas[i][1])
        lar4.append(lar1-coordenadas[i][0])
        x2=coordenadas[i][1]
        y2=coordenadas[i][0]
        x21=0
        y21=0
        while x2 != lar2:
            x2+=1
            x21+=1
        while y2 != lar1:
            y2+=1
            y21+=1
        temp=min(x21,y21)
        lar5.append(temp)
    x=[]
    y=[]
    z=[]
    top=0
    for i in range(len(coordenadas)):
        x.append([])
        y.append([])
        z.append([])
        for x1 in range(lar3[top]):
            x[i].append(lista[coordenadas[i][0]][coordenadas[i][1]+x1])
        for y1 in range(lar4[top]):
            y[i].append(lista[coordenadas[i][0]+y1][coordenadas[i][1]])
        for z1 in range(lar5[top]):
            z[i].append(lista[coordenadas[i][0]+z1][coordenadas[i][1]+z1])
        top+=1
    temp=[]
    for i in range(len(temporal1)):
        temp.append([])
        for r in temporal1[i]:
            temp[i].append(r)
    final=[]
    for i in range(len(temporal1)):
        for e in range(len(coordenadas)):
            if temp[i] == x[e]:
                final.append((palabras[i],coordenadas[i],"derecha"))
                break
            if temp[i] == y[e]:
                final.append((palabras[i],coordenadas[i],"abajo"))
                break
            if temp[i] == z[e]:
                final.append((palabras[i],coordenadas[i],"diagonal"))
                break
    archivo.close()
    return(final)

if __name__=="__main__":
    print(sopaletras("sopa.txt",["cra"]))
    print(sopaletras("sopa.txt", ["aro"]))
    print(sopaletras("sopa.txt", ["casa"]))
    print(sopaletras("sopa.txt",["casa","cra","aro"]))

           