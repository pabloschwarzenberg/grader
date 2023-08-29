def sopaletras(nombre_archivo,palabras):
    archivo=open(nombre_archivo,"r")
    p=[]
    s=""
    for linea in archivo:
        filas=linea.lower().strip().split("\n")
        s="".join(filas)
        s=s.split(" ")
        p.append(s)
    archivo.close()
    l=[]
    for i in palabras:
        j=0
        inicial=i[0]
        coincidencias=[]
        for k in range(len(p[0])):
            if p[j][k]==inicial:
                coincidencias.append([j,k])
        t=0
        while t<len(coincidencias):
            if len(i)<=len(p): #and ver cuando no está en los bordes:
                h=coincidencias[t][0]+1
                m=coincidencias[t][1]
                while h<len(i):
                    if i[h]==p[h][m]:
                        h=h+1
                    else:
                        h=len(i)+1
                while h==len(i):
                    l.append((i,coincidencias[t],"abajo"))
                    h=h+1
            if len(i)<=len(p[0]): #lo mismo que arriba
                h=coincidencias[t][1]+1
                m=coincidencias[t][0]
                while h<len(i):
                    if i[h]==p[m][h]:
                        h=h+1
                    else:
                        h=len(i)+1
                while h==len(i):
                    l.append((i,coincidencias[t],"derecha"))
                    h=h+1
            if len(i)<=len(p) and len(i)<=len(p[0]):
                h=coincidencias[t][1]+1
                m=coincidencias[t][0]+1
                while h<len(i):
                    if i[h]==p[m][h]:
                        h=h+1
                        m=m+1
                    else:
                        h=len(i)+1
                while h==len(i):
                    l.append((i,coincidencias[t],"diagonal"))
                    h=h+1
                t=t+1
            else:
                t=t+1
    return l

if __name__=="__main__":
    palabras=["casa","cra","aro"]
    print(sopaletras("sopa.txt",palabras))