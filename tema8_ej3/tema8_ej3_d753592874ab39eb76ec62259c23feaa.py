hombre_imaginario = """
El hombre imaginario
vive en una mansión imaginaria
rodeada de árboles imaginarios
a la orilla de un río imaginario

De los muros que son imaginarios
penden antiguos cuadros imaginarios
irreparables grietas imaginarias
que representan hechos imaginarios
ocurridos en mundos imaginarios
en lugares y tiempos imaginarios

Todas las tardes tardes imaginarias
sube las escaleras imaginarias
y se asoma al balcón imaginario
a mirar el paisaje imaginario
que consiste en un valle imaginario
circundado de cerros imaginarios..."""

def estadisticas_frase(frase):
    #Retornar el número de palabras
    frase2=frase
    frase22=frase2.split()
    lista_palabras=frase.splitlines()
    lista_palabras=" ".join(lista_palabras)
    lista_palabras=lista_palabras.split(" ")
    lista_palabras=" ".join(lista_palabras)
    lista_palabras=lista_palabras.lstrip(" ")#### puedo usarlo si le quito el pto suspensivo
    lista_palabras1=lista_palabras.split(" ")
    

    cantidad_palabras=0                ###Cantidad de palabras
    for o in lista_palabras1:
        if o!="":
            cantidad_palabras+=1
    
    cantidad_letras=0                       ##Cantidad de letras sin espacios
    cantidad_letras2=0                      

    
    for i in lista_palabras:
        cantidad_letras2+=1
        for h in i:
            if h!=" " and h!=".":
                cantidad_letras+=1
                
    lista=[]                         ### Lista de letras y puntos por separado
    for t in lista_palabras:
        if t!=" ":
            lista.append(t)

    largo_palabras=0
    largo_palabras2=[]
    u=0
    for p in lista_palabras1:
        u+=1
        for e in p:
            if e!=".":
                y=len(p)
        largo_palabras2.append(y)
        largo_palabras+=y

    w=0                              ##Cantidad de carácteres
    for e in frase2:
        w+=1

    l=0
    ss=[]
    for q in frase22:
        for ñ in q:
            if ñ==".":
                a=list(q)
                h=a.count(".")
                for n in range(h):
                    a.remove(".")
                q="".join(a)
                
        ss.append(q)

    
    z=0
    largo_palabras3=[]
    for m in ss:
        yy=len(m)
        largo_palabras3.append(yy)
        z+=yy
    
    #promedio_largo_palabras=largo_palabras/cantidad_palabras
    promedio_largo_palabras2=z/cantidad_palabras                   ### Promedio de largo de palabras

    ww=0                                                         ### Cuantos signos de puntuación hay
    for xx in lista_palabras1:
        for x in xx:
            if x=="." or x=="," or x==";":
                ww+=1

    dan=0
    for jj in frase2:
        if jj==" ":
            dan+=1

    #ss, lista_palabras1, lista_palabras, largo_palabras3, z, promedio_largo_palabras2, largo_palabras2, largo_palabras, promedio_largo_palabras, cantidad_palabras, cantidad_letras2, w
    return(cantidad_palabras, w, promedio_largo_palabras2, dan, ww)

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         