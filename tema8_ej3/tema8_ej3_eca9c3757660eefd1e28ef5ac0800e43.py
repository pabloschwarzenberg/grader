def estadisticas_frase(s):
    numerop=s.split()
    palabras=0
    letra=0
    prome=0
    separa=0
    puntuacion=0
    letra=len(s)
    for palabra in numerop:
        if palabra not in "...,!?":
           palabras+=1
    reemplazo=(("ó","o"),("í","i"),("á","a"))
    for a,b in reemplazo:
        nueva=s.replace(a,b)
    for promedio in nueva:
        if (promedio.isalpha()):
           prome+=1
    media=prome/palabras         
    for espacio in s:
        if espacio in " ":
            separa+=1
    for punto in s:
        if punto==".":
            puntuacion+=1
            
    return palabras,letra,media,separa,puntuacion
   