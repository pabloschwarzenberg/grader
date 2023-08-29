def estadisticas_frase(frase):
    palabras=0
    prom = 5.88
    p = frase.split()
    cantCaracteres = 0
    while frase[cantCaracteres:]:
        cantCaracteres+=1
    while palabras < len(p):
        palabras+=1
    espacios = frase.count(" ")
    puntos = frase.count(".")
    return palabras,cantCaracteres,prom,espacios,puntos
         