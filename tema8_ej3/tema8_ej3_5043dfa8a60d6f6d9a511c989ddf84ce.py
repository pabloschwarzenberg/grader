def estadisticas_frase(frase):
    L1=list(frase)
    frase=frase.replace("\n"," ")
    L=frase.split(" ")
    largo=len(L)
    for i in range(largo-3):
        if L[i]=="":
            L.pop(i)
            largo-=1
        else:
            pass   
    cant_palabras=len(L)
    cant_caracteres=len(L1)
    cant_espacios=L1.count(" ")
    comas=L1.count(",")
    puntos=L1.count(".")
    puntocoma=L1.count(";")
    cant_puntuacion=comas+puntos+puntocoma
    suma=0
    for i in range(cant_palabras):
        suma+=len(L[i])
    suma-=cant_puntuacion
    promedio_palabras=suma/len(L)



    return cant_palabras,cant_caracteres,promedio_palabras,cant_espacios,cant_puntuacion


