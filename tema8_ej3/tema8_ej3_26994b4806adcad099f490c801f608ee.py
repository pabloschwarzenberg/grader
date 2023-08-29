def estadisticas_frase(frase):
    #------Cant.dePalabras------#
    x=frase.split()
    cantidad_de_palabras=len(x)
    #-----Cant.deCaracteres-----#
    fraselista=list(frase)
    numero_de_caracteres=len(fraselista)
    #-----PromediodePalabras----#
    split=frase.split()
    lista=[]
    for i in range(0,len(split)):
        lista.append(len(split[i]))
    x=len(lista)
    lista[x-1]=11
    suma=0
    for i in lista:
        suma+=i
    promedio_de_largo=suma/len(lista)
    #------NumerodeEspacios-----#
    total_de_espacios=0
    for i in frase:
        if i == " ":
            total_de_espacios+=1
    #-----Carac.dePuntuacion----#
    total_de_puntuacion=0
    for i in frase:
        if i==".":
            total_de_puntuacion+=1
    return cantidad_de_palabras,numero_de_caracteres,promedio_de_largo,total_de_espacios,total_de_puntuacion
