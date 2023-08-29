def estadisticas_frase(frase):
    #numero de palabras X
    #numero de caracteres X
    #largo promedio palabras
    #numero de espacios
    #numero de caracteres de puntuacion
    frase=frase.lower()
    frase1=list(frase)
    frase=list(frase)
    while "." in frase:
        frase.remove(".")
    frase="".join(frase)
    palabras_frase=frase.split()
    letras=["a","b","c","d","e","f","g","h","i","j","k","m","n","ñ","o","p","q","r","s","t","u","w","x","y","z","á","é","í","ó","ú"]
    n_letras=0
    n_espacios=0
    n_puntuacion=0
    n_caracteres=len(frase1)
    palabras=len(palabras_frase)
    contador=0
    for i in range(0,len(frase1)):
        if frase1[i] in letras:
            n_letras=n_letras+1
            contador=contador+1
        elif frase1[i]==" ":
            n_espacios=n_espacios+1
            contador=0
        elif frase1[i]==".":
            n_puntuacion=n_puntuacion+1
    suma=0
    for i in range(0,len(palabras_frase)):
        suma=suma+len(palabras_frase[i])
    promedio=suma/palabras
        
    return (palabras,n_caracteres,promedio,n_espacios,n_puntuacion)

         