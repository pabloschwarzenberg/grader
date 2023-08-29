def sopaletras(nombre_archivo,palabras):
    archivo=open(nombre_archivo,"r")
    archivo.close()
    return [(palabras[0],[0,0],"diagonal")]

def posysent(palabr,posisi):
    posis=[posisi]
    palabra=palabr.upper()
    k=0
    j=0
    posib=[]
    ini=[]
    pos_ini=[]
    pos=[]
    letras=[]
    for l in posis[0]:
        letras.append(l[0])
    for l in palabra:
        for li in posis[0]:
            if li[0]==l and l==palabra[0]:
                ini.append([li[1]])
            elif li[0]==l:
                posib.append(li[1])
    k=0
    j=0
    while k<len(ini):
        j=0
        while j<len(posib):
           
            if ini[k][-1][0]+1==posib[j][0] and ini[k][-1][1]+1==posib[j][1]:
                ini[k].append(posib[j])
            elif ini[k][-1][0]==posib[j][0] and ini[k][-1][1]+1==posib[j][1]:
                ini[k].append(posib[j])
            elif ini[k][-1][0]+1==posib[j][0] and ini[k][-1][1]==posib[j][1]:
                ini[k].append(posib[j])
            j=j+1
        k=k+1
    for n in ini:
        if len(n)==len(palabra):
            pos=n
    sentido="hola"
    if pos[0][0]==pos[-1][0] and pos[0][1]==(pos[-1][1]-len(palabra)+1):
        sentido="derecha"
    elif pos[0][1]==pos[-1][1] and pos[0][0]==(pos[-1][0]-len(palabra)+1):
        sentido="abajo"
    elif pos[0][1]==(pos[-1][1]-len(palabra)+1) and (pos[0][0]==pos[-1][0]-len(palabra)+1):
        sentido="diagonal"
    return [pos[0],sentido]

def sopaletras(nombre_archivo,palabras):
    archivo=open(nombre_archivo,"r")
    ar=list(archivo.readlines())
    sopa=[]
    l1=[]
    pala=[]
    k=0
    posiciones=[]
    posis=[]
    while k<len(ar):
        a=ar[k].split(" ")
        a[-1]=a[-1][0]
        sopa.append(a)
        k=k+1
    for n in palabras:
        a=n.upper()
        pala.append(n)
        l1.append(list(a))

    for palabr in l1:
        posiciones=[]
        for letra in palabr:
            k=0
            for linea in sopa:
                j=0
                for l in linea:
                    if letra == l and [palabr,letra,k,j] not in posiciones:
                        posiciones.append([letra,[k,j]])
                    j=j+1
                k=k+1
        posis.append(posiciones)
    k=0
    respuesta=[]
    while k<len(pala):
        a=pala[k]
        b=posis[k]
        c=posysent(a,b)
        d=(a,c[0],c[1])
        if len(palabras)>1:
            respuesta.append(d)
        else:
            return d
        k=k+1
    archivo.close()
    return respuesta

if __name__=="__main__":
    print(sopaletras("sopa.txt",["cra"]))
    print(sopaletras("sopa.txt", ["aro"]))
    print(sopaletras("sopa.txt", ["casa"]))
    print(sopaletras("sopa.txt",["casa","cra","aro"]))

           