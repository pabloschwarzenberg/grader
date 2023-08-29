def sopaletras(nombre_archivo,palabras):
    sopa=["casa","cra","aro"]
    lista=list["0","1","i","j"]
    for palabras in sopa:
        if palabras==cra:
            lista[2],lista[3]=lista[0],lista[0]
            posicion="diagonal"
        if palabras==casa:
            lista[2],lista[3]=lista[0],lista[0]
            posicion="derecha"
        if palabras==aro:
            lista[2],lista[3]=lista[0],lista[1]
            posicion="abajo"
    return [(palabras,lista[2],lista[3],posicion)]

